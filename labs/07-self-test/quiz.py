import argparse
import csv
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[2]


def load_bank(language, path=None):
    if language not in ("en", "fr"):
        raise ValueError("Unknown language / Langue inconnue")
    source = Path(path) if path is not None else Path(__file__).with_name(f"questions.{language}.csv")
    with source.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["id", "question", "answer", "module", "section"]:
            raise ValueError("Invalid columns / Colonnes invalides")
        bank = list(reader)
    seen = set()
    for row in bank:
        if set(row) != {"id", "question", "answer", "module", "section"} or any(
                not isinstance(value, str) or not value.strip() for value in row.values()):
            raise ValueError("Empty or invalid field / Champ vide ou invalide")
        target = (ROOT / row["module"]).resolve()
        if not target.is_relative_to(ROOT / "docs" / language) or not target.is_file():
            raise ValueError("Invalid module / Module invalide")
        if "## " + row["section"] not in target.read_text(encoding="utf-8").splitlines():
            raise ValueError("Missing section / Section absente")
        if row["id"] in seen:
            raise ValueError("Duplicate identity / Identité dupliquée")
        seen.add(row["id"])
    if len(bank) < 30:
        raise ValueError("At least 30 questions / Au moins 30 questions")
    return bank


def select_questions(bank, count, seed=None):
    if type(count) is not int or not 1 <= count <= len(bank):
        raise ValueError("Invalid question count / Nombre de questions invalide")
    return random.Random(seed).sample(bank, count)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Original module questions / Questions originales sur les modules")
    parser.add_argument("--lang", choices=("en", "fr"), default="en")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--show-answers", action="store_true")
    args = parser.parse_args(argv)
    try:
        questions = select_questions(load_bank(args.lang), args.count, args.seed)
        print("Not an official exam simulator." if args.lang == "en" else "Ce n'est pas un simulateur d'examen officiel.")
        for index, row in enumerate(questions, 1):
            print(f"{index}. [{row['id']}] {row['question']}")
            if not args.show_answers:
                input("Write your answer, then press Enter: " if args.lang == "en" else "Écris ta réponse, puis Entrée : ")
            print(("Suggested answer: " if args.lang == "en" else "Correction proposée : ") + row["answer"])
            print(f"{row['module']} > {row['section']}")
        return 0
    except (OSError, ValueError, EOFError) as error:
        print(f"Error / Erreur: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
