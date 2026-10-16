import json
from pathlib import Path
import sys


def load_events():
    return json.loads(Path(__file__).with_name("events.json").read_text(encoding="utf-8"))


def replay(events, idempotent=True):
    if not isinstance(events, list) or not events:
        raise ValueError("Invalid trace / Trace invalide")
    result = {"credits": 0, "applied": [], "duplicates": [], "out_of_order": [], "late": [], "pending": []}
    required = {"id", "incident", "agreement", "sequence", "kind", "occurred", "received", "credits"}
    seen, sequences, pending = {}, {}, {}
    next_sequence, highest = 1, 0
    scope = None
    state = None
    for event in events:
        if not isinstance(event, dict) or set(event) != required:
            raise ValueError("Invalid event fields / Champs invalides")
        for field in ("id", "incident", "agreement"):
            if not isinstance(event[field], str) or not event[field].strip():
                raise ValueError("Invalid reference / Référence invalide")
        for field in ("sequence", "occurred", "received", "credits"):
            if type(event[field]) is not int or event[field] < 0:
                raise ValueError("Invalid number / Nombre invalide")
        if event["sequence"] < 1 or event["received"] < event["occurred"]:
            raise ValueError("Invalid chronology / Chronologie invalide")
        if event["kind"] not in ("opened", "restored", "adjusted", "reviewed"):
            raise ValueError("Invalid kind / Nature invalide")
        if event["kind"] != "adjusted" and event["credits"] != 0:
            raise ValueError("Unexpected credits / Crédits inattendus")
        event_scope = (event["incident"], event["agreement"])
        if scope is not None and scope != event_scope:
            raise ValueError("One incident per trace / Un incident par trace")
        scope = event_scope
        reference, sequence = event["id"], event["sequence"]
        signature = {k: v for k, v in event.items() if k != "received"}
        if reference in seen and signature != seen[reference]:
            raise ValueError("Conflicting duplicate / Doublon contradictoire")
        if sequence in sequences and sequences[sequence] != reference:
            raise ValueError("Conflicting sequence / Séquence contradictoire")
        if event["received"] - event["occurred"] > 10:
            result["late"].append(reference)
        if reference in seen:
            result["duplicates"].append(reference)
            if idempotent:
                continue
        elif sequence < highest:
            result["out_of_order"].append(reference)
        highest = max(highest, sequence)
        seen[reference] = signature
        sequences[sequence] = reference
        if not idempotent:
            result["credits"] += event["credits"]
            result["applied"].append(reference)
            continue
        pending[sequence] = event
        while next_sequence in pending:
            current = pending.pop(next_sequence)
            expected = {None: "opened", "opened": "restored", "restored": "adjusted", "adjusted": "reviewed"}
            if current["kind"] != expected.get(state):
                raise ValueError("Invalid transition / Transition invalide")
            state = current["kind"]
            result["credits"] += current["credits"]
            result["applied"].append(current["id"])
            next_sequence += 1
    result["pending"] = sorted(pending)
    return result


def main():
    try:
        events = load_events()
        print("Synthetic trace / Trace synthétique")
        for mode, label in ((False, "Naive / Naïf"), (True, "Idempotent and ordered / Idempotent et ordonné")):
            result = replay(events, idempotent=mode)
            print(label)
            for key, translation in (("credits", "crédits"), ("applied", "appliqués"),
                    ("duplicates", "doublons"), ("out_of_order", "hors ordre"),
                    ("late", "tardifs"), ("pending", "en attente")):
                print(f"{key} / {translation}: {result[key]}")
        return 0
    except (OSError, ValueError) as error:
        print(f"Error / Erreur: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
