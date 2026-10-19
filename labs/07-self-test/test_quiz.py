import csv
from pathlib import Path
import tempfile
import unittest
from quiz import load_bank, select_questions


class QuizTests(unittest.TestCase):
    def test_banks_have_thirty_three_paired_original_items(self):
        en, fr = load_bank("en"), load_bank("fr")
        self.assertEqual(len(en), 33)
        self.assertEqual([q["id"] for q in en], [q["id"] for q in fr])
        self.assertTrue(all(q["question"] != f["question"] for q, f in zip(en, fr)))

    def test_selection_is_unique_and_reproducible(self):
        bank = load_bank("en")
        first = select_questions(bank, 7, 12)
        self.assertEqual(first, select_questions(bank, 7, 12))
        self.assertEqual(len({q["id"] for q in first}), 7)

    def test_all_items_can_be_selected(self):
        self.assertEqual(len(select_questions(load_bank("fr"), 33, 1)), 33)

    def test_invalid_counts_fail(self):
        for count in (0, -1, 34, True):
            with self.subTest(count=count), self.assertRaises(ValueError):
                select_questions(load_bank("en"), count, 1)

    def test_unknown_language_fails(self):
        with self.assertRaises(ValueError):
            load_bank("xx")

    def test_invalid_reference_and_duplicate_id_fail(self):
        bank = load_bank("en")
        for field, value in (("module", "missing.md"), ("section", "Missing heading"), ("id", bank[1]["id"])):
            rows = [dict(row) for row in bank]
            rows[0][field] = value
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "bank.csv"
                with path.open("w", newline="", encoding="utf-8") as stream:
                    writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
                    writer.writeheader()
                    writer.writerows(rows)
                with self.subTest(field=field), self.assertRaises(ValueError):
                    load_bank("en", path)


if __name__ == "__main__":
    unittest.main()
