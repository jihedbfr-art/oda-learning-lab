"""Read a synthetic catalogue / Lire un catalogue synthétique. Standard library only."""
import json
from pathlib import Path
import sys


def validate(data):
    """Check this exercise's rules / Vérifier les règles de cet exercice."""
    try:
        specifications = data["specifications"]
        offers = data["offers"]
        if not isinstance(specifications, list) or not isinstance(offers, list):
            raise ValueError
        if not specifications or not offers:
            raise ValueError
        spec_ids = set()
        for spec in specifications:
            reference = spec["id"]
            services = spec["services"]
            if not isinstance(reference, str) or not reference or reference in spec_ids:
                raise ValueError
            if not isinstance(services, list) or not services:
                raise ValueError
            if any(not isinstance(service, str) or not service for service in services):
                raise ValueError
            spec_ids.add(reference)
        offer_ids = set()
        for offer in offers:
            reference = offer["id"]
            if not isinstance(reference, str) or not reference or reference in offer_ids:
                raise ValueError
            offer_ids.add(reference)
            if offer["specification"] not in spec_ids:
                raise ValueError
            amount = offer["price"]["credits"]
            if type(amount) is not int or amount < 0:
                raise ValueError
            if offer["price"]["period"] != "month":
                raise ValueError
        return len(offers)
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("Invalid catalogue / Catalogue invalide") from error


def main():
    """Display local data without changing it / Afficher sans modifier les données."""
    try:
        data = json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8-sig"))
        count = validate(data)
    except (OSError, ValueError) as error:
        print(f"Error / Erreur: {error}", file=sys.stderr)
        return 1
    print("Synthetic data / Données synthétiques")
    print(f"Valid offers / Offres valides: {count}")
    specs = {spec["id"]: spec for spec in data["specifications"]}
    for offer in data["offers"]:
        services = ", ".join(specs[offer["specification"]]["services"])
        print(f"{offer['id']} | {offer['specification']} | {services} | {offer['price']['credits']} credits/month (crédits/mois)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
