"""Catalogue behaviour tests / Tests de comportement du catalogue."""
import copy
import json
from pathlib import Path
import unittest
from catalog import validate

DATA = json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8-sig"))


class CatalogTests(unittest.TestCase):
    def test_sample_has_four_valid_offers(self):
        self.assertEqual(validate(DATA), 4)

    def test_unknown_specification_is_rejected(self):
        data = copy.deepcopy(DATA)
        data["offers"][0]["specification"] = "missing"
        with self.assertRaises(ValueError):
            validate(data)

    def test_duplicate_offer_is_rejected(self):
        data = copy.deepcopy(DATA)
        data["offers"].append(data["offers"][0])
        with self.assertRaises(ValueError):
            validate(data)

    def test_invalid_amounts_are_rejected(self):
        for amount in (-1, True, 2.5, "12", None):
            with self.subTest(amount=amount):
                data = copy.deepcopy(DATA)
                data["offers"][0]["price"]["credits"] = amount
                with self.assertRaises(ValueError):
                    validate(data)

    def test_missing_or_empty_name_is_rejected(self):
        for name in ({"en": "Talk"}, {"en": "Talk", "fr": ""}, {"en": 1, "fr": "x"}, "Talk"):
            with self.subTest(name=name):
                data = copy.deepcopy(DATA)
                data["offers"][0]["name"] = name
                with self.assertRaises(ValueError):
                    validate(data)

    def test_invalid_structure_is_rejected(self):
        for data in ({}, {"specifications": [], "offers": []}, [], None, "x", 42):
            with self.subTest(data=data), self.assertRaises(ValueError):
                validate(data)


if __name__ == "__main__":
    unittest.main()
