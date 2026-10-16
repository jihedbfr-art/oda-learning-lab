import json


def describe():
    return {
        "name": "order-desk",
        "responsibilities": {
            "en": ["Check a setup request", "Retain the agreement reference"],
            "fr": ["Vérifier une demande de préparation", "Conserver la référence de l'accord"],
        },
        "exposes": {"prepare": {
            "required": {"agreement": "non-empty string", "offer": "non-empty string"},
            "returns": {"agreement": "same reference", "state": "prepared"},
        }},
        "consumes": {"offer-shelf": {"operation": "read-offer"}},
    }


def prepare(request, dependencies):
    contract = describe()
    required = contract["exposes"]["prepare"]["required"]
    if not isinstance(request, dict) or set(request) != set(required):
        raise ValueError("Invalid request / Demande invalide")
    if any(not isinstance(value, str) or not value.strip() for value in request.values()):
        raise ValueError("Invalid request / Demande invalide")
    if not isinstance(dependencies, set) or any(not isinstance(dep, str) for dep in dependencies):
        raise ValueError("Invalid dependencies / Dépendances invalides")
    declared = set(contract["consumes"])
    if dependencies - declared:
        raise ValueError("Undeclared dependency / Dépendance non déclarée")
    if declared - dependencies:
        raise ValueError("Missing dependency / Dépendance manquante")
    return {"agreement": request["agreement"], "state": "prepared"}


if __name__ == "__main__":
    print(json.dumps(describe(), ensure_ascii=False, indent=2))
    print(json.dumps(prepare({"agreement": "agreement-A", "offer": "offer-B"}, {"offer-shelf"})))
