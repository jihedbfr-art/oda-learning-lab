import copy
import unittest
from component import describe, prepare


class ComponentTests(unittest.TestCase):
    def setUp(self):
        self.request = {"agreement": "agreement-A", "offer": "offer-B"}

    def test_declares_responsibilities_and_both_contracts(self):
        declaration = describe()
        self.assertTrue(declaration["responsibilities"]["en"])
        self.assertTrue(declaration["responsibilities"]["fr"])
        self.assertIn("prepare", declaration["exposes"])
        self.assertIn("offer-shelf", declaration["consumes"])

    def test_valid_request_retains_agreement(self):
        self.assertEqual(prepare(self.request, {"offer-shelf"}),
                         {"agreement": "agreement-A", "state": "prepared"})

    def test_every_required_field_is_checked(self):
        for field in self.request:
            request = self.request.copy()
            del request[field]
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "Invalid request"):
                prepare(request, {"offer-shelf"})

    def test_wrong_types_and_empty_references_are_rejected(self):
        for field in self.request:
            for value in (None, True, 3, [], "", "   "):
                request = dict(self.request, **{field: value})
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    prepare(request, {"offer-shelf"})

    def test_undeclared_dependency_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Undeclared dependency"):
            prepare(self.request, {"offer-shelf", "charge-desk"})

    def test_required_dependency_must_be_present(self):
        with self.assertRaisesRegex(ValueError, "Missing dependency"):
            prepare(self.request, set())

    def test_unknown_fields_and_invalid_container_are_rejected(self):
        for request in ([], None, dict(self.request, secret="synthetic")):
            with self.subTest(request=request), self.assertRaises(ValueError):
                prepare(request, {"offer-shelf"})

    def test_description_and_request_are_not_mutated(self):
        original = copy.deepcopy(self.request)
        declaration = describe()
        declaration["consumes"].clear()
        prepare(self.request, {"offer-shelf"})
        self.assertEqual(self.request, original)
        self.assertIn("offer-shelf", describe()["consumes"])


if __name__ == "__main__":
    unittest.main()
