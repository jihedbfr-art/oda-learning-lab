import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from drift import compare


SCRIPT = Path(__file__).with_name("drift.py")


def declaration(fields):
    return {"exposes": {"prepare": {"fields": fields}}}


def field(kind="string", required=True):
    return {"type": kind, "required": required}


class DriftTests(unittest.TestCase):
    def test_empty_and_unchanged_declarations(self):
        self.assertEqual(compare({}, {"exposes": {}}), [])
        contract = declaration({"agreement": field()})
        self.assertEqual(compare(contract, copy.deepcopy(contract)), [])

    def test_optional_field_added_is_compatible(self):
        result = compare(declaration({}), declaration({"note": field(required=False)}))
        self.assertEqual([(r["code"], r["classification"], r["path"]) for r in result],
                         [("optional-field-added", "compatible", ["exposes", "prepare", "fields", "note"])])

    def test_required_field_added_needs_review(self):
        self.assertEqual(compare(declaration({}), declaration({"agreement": field()}))[0]["classification"], "review")

    def test_optional_becoming_required_needs_review(self):
        result = compare(declaration({"note": field(required=False)}), declaration({"note": field()}))
        self.assertEqual([(r["code"], r["classification"]) for r in result], [("field-required", "review")])

    def test_required_becoming_optional_is_compatible(self):
        result = compare(declaration({"note": field()}), declaration({"note": field(required=False)}))
        self.assertEqual(result[0]["classification"], "compatible")

    def test_type_widening_needs_review(self):
        for before, after in [("string", ["string", "null"]), ("integer", "number")]:
            with self.subTest(before=before):
                result = compare(declaration({"value": field(before)}), declaration({"value": field(after)}))
                self.assertEqual([(r["code"], r["classification"]) for r in result], [("type-widened", "review")])

    def test_type_change_and_narrowing_are_breaking(self):
        for before, after in [("string", "integer"), (["string", "null"], "string"), ("number", "integer")]:
            with self.subTest(before=before):
                self.assertEqual(compare(declaration({"value": field(before)}),
                                         declaration({"value": field(after)}))[0]["classification"], "breaking")

    def test_union_order_and_numeric_equivalence_are_not_changes(self):
        for before, after in [(["null", "string"], ["string", "null"]), ("number", ["integer", "number"])]:
            with self.subTest(before=before):
                self.assertEqual(compare(declaration({"value": field(before)}), declaration({"value": field(after)})), [])

    def test_operation_removal_reports_boundary_once(self):
        result = compare(declaration({"agreement": field()}), {})
        self.assertEqual([(r["code"], r["classification"], r["path"]) for r in result],
                         [("operation-removed", "breaking", ["exposes", "prepare"])])

    def test_operation_addition_is_compatible(self):
        self.assertEqual(compare({}, declaration({"agreement": field()}))[0]["classification"], "compatible")

    def test_required_field_removal_is_breaking(self):
        self.assertEqual(compare(declaration({"agreement": field()}), declaration({}))[0]["classification"], "breaking")

    def test_optional_field_removal_needs_review(self):
        self.assertEqual(compare(declaration({"note": field(required=False)}), declaration({}))[0]["classification"], "review")

    def test_each_changed_property_is_reported_without_mutation(self):
        before = declaration({"agreement": field(required=False)})
        after = declaration({"agreement": field("integer")})
        saved = copy.deepcopy((before, after))
        result = compare(before, after)
        self.assertEqual([r["code"] for r in result], ["field-required", "type-changed"])
        self.assertEqual((before, after), saved)
        self.assertTrue(all(r["message"]["en"] and r["message"]["fr"] for r in result))

    def test_unknown_type_rejected_even_in_removed_operation(self):
        for kind in ("mystery", ["string", "mystery"]):
            bad = declaration({"value": field(kind)})
            for before, after in ((bad, {}), ({}, bad)):
                with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "Unknown type / Type inconnu"):
                    compare(before, after)

    def test_malformed_declarations_are_not_silently_ignored(self):
        invalid = [None, [], {"extra": {}}, {"exposes": []}, {"exposes": {" ": {"fields": {}}}},
                   {"exposes": {"prepare": {}}}, {"exposes": {"prepare": {"fields": {}, "returns": {}}}},
                   declaration({"": field()}), declaration({"value": {"type": "string"}}),
                   declaration({"value": field(required=1)}), declaration({"value": field([])}),
                   declaration({"value": field(["string", "string"])}), declaration({"value": field({})})]
        for bad in invalid:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                compare({}, bad)

    def test_sample_cli_from_another_directory_is_bilingual(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT.resolve())], cwd=directory,
                                    capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("compatible / compatible", result.stdout)
        self.assertIn("review / à examiner", result.stdout)
        self.assertIn("breaking / rupture", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_invalid_sample_file_returns_two_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.json"
            for content in ('{', json.dumps({"before": {}, "after": declaration({"x": field("mystery")})}),
                            json.dumps({"before": {}})):
                path.write_text(content, encoding="utf-8")
                result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), str(path)],
                                        capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, 2)
                self.assertIn("Error / Erreur", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
