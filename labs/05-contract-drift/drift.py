import argparse
import json
from pathlib import Path
import sys


TYPES = {"string", "integer", "number", "boolean", "null", "array", "object"}
LABELS = {"compatible": "compatible / compatible", "review": "review / à examiner", "breaking": "breaking / rupture"}
RULES = {
    "operation-added": ("compatible", "Operation added", "Opération ajoutée"),
    "operation-removed": ("breaking", "Operation removed", "Opération retirée"),
    "optional-field-added": ("compatible", "Optional field added", "Champ optionnel ajouté"),
    "required-field-added": ("review", "Required field added", "Champ obligatoire ajouté"),
    "required-field-removed": ("breaking", "Required field removed", "Champ obligatoire retiré"),
    "optional-field-removed": ("review", "Optional field removed", "Champ optionnel retiré"),
    "field-required": ("review", "Field became required", "Champ devenu obligatoire"),
    "field-optional": ("compatible", "Field became optional", "Champ devenu optionnel"),
    "type-widened": ("review", "Type widened", "Type élargi"),
    "type-changed": ("breaking", "Type changed or narrowed", "Type changé ou restreint"),
}


def type_set(kind):
    kinds = [kind] if isinstance(kind, str) else kind
    if not isinstance(kinds, list) or not kinds or any(not isinstance(k, str) for k in kinds):
        raise ValueError("Invalid type / Type invalide")
    if any(k not in TYPES for k in kinds):
        raise ValueError("Unknown type / Type inconnu")
    if len(set(kinds)) != len(kinds):
        raise ValueError("Duplicate type / Type dupliqué")
    result = set(kinds)
    if "number" in result:
        result.add("integer")
    return result


def validate(declaration):
    if not isinstance(declaration, dict) or set(declaration) not in (set(), {"exposes"}):
        raise ValueError("Invalid declaration / Déclaration invalide")
    operations = declaration.get("exposes", {})
    if not isinstance(operations, dict):
        raise ValueError("Invalid operations / Opérations invalides")
    for name, operation in operations.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid operation name / Nom d'opération invalide")
        if not isinstance(operation, dict) or set(operation) != {"fields"} or not isinstance(operation["fields"], dict):
            raise ValueError("Invalid operation / Opération invalide")
        for name, field in operation["fields"].items():
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Invalid field name / Nom de champ invalide")
            if not isinstance(field, dict) or set(field) != {"type", "required"} or type(field["required"]) is not bool:
                raise ValueError("Invalid field / Champ invalide")
            type_set(field["type"])
    return operations


def compare(before, after):
    old, new = validate(before), validate(after)
    findings = []

    def report(code, path):
        classification, en, fr = RULES[code]
        findings.append({"code": code, "classification": classification, "path": path,
                         "message": {"en": en, "fr": fr}})

    for name in sorted(old.keys() | new.keys()):
        path = ["exposes", name]
        if name not in old:
            report("operation-added", path)
            continue
        if name not in new:
            report("operation-removed", path)
            continue
        old_fields, new_fields = old[name]["fields"], new[name]["fields"]
        for name in sorted(old_fields.keys() | new_fields.keys()):
            field_path = path + ["fields", name]
            if name not in old_fields:
                report("required-field-added" if new_fields[name]["required"] else "optional-field-added", field_path)
                continue
            if name not in new_fields:
                report("required-field-removed" if old_fields[name]["required"] else "optional-field-removed", field_path)
                continue
            previous, current = old_fields[name], new_fields[name]
            if previous["required"] != current["required"]:
                report("field-required" if current["required"] else "field-optional", field_path + ["required"])
            old_types, new_types = type_set(previous["type"]), type_set(current["type"])
            if old_types != new_types:
                report("type-widened" if old_types < new_types else "type-changed", field_path + ["type"])
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare invented contracts / Comparer des contrats inventés")
    parser.add_argument("sample", nargs="?", type=Path, default=Path(__file__).with_name("drift_samples.json"),
                        help="JSON with before and after / JSON avec before et after")
    args = parser.parse_args(argv)
    try:
        sample = json.loads(args.sample.read_text(encoding="utf-8"))
        if not isinstance(sample, dict) or set(sample) != {"before", "after"}:
            raise ValueError("Expected before and after / before et after attendus")
        findings = compare(sample["before"], sample["after"])
        print("Declared changes only / Changements déclarés uniquement")
        for finding in findings:
            path = json.dumps(finding["path"], ensure_ascii=False)
            print(f"{LABELS[finding['classification']]}: {path}: "
                  f"{finding['message']['en']} / {finding['message']['fr']}")
        if not findings:
            print("No declared change / Aucun changement déclaré")
        return 0
    except (OSError, ValueError) as error:
        print(f"Error / Erreur: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
