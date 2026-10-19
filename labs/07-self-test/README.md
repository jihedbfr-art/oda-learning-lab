# Module self-assessment

[Version française](README.fr.md)

This is not an official exam simulator. Thirty-three original English questions and thirty-three French questions cover only this repository's Modules 1–6. No exam question content was used. See [Module 7](../../docs/en/07-preparing-for-certification.md).

## Run

Python 3.9 or later, standard library only. From the repository root:

```console
python labs/07-self-test/quiz.py --lang en --count 5
python labs/07-self-test/quiz.py --lang fr --count 5
python labs/07-self-test/quiz.py --lang en --count 33 --seed 7 --show-answers
python -m unittest discover -s labs/07-self-test -p test_quiz.py
python tools/check_docs.py
```

Interactive mode waits for your answer before showing a suggested correction and module/section reference. It does not grade the text you enter. `--show-answers` displays corrections immediately for reading or non-interactive verification. `--seed` makes selection reproducible within the same Python environment; a draw contains no duplicates.

## Read and validate the bank

[questions.en.csv](questions.en.csv) and [questions.fr.csv](questions.fr.csv) share identities, five per module plus three about contract drift in Module 5. Columns: `id`, `question`, `answer`, `module`, `section`. Module paths are relative to the root; sections use their exact headings. Loading checks columns, non-empty fields, unique identities, at least thirty questions, existing modules and headings in the selected language.

Executed on 2026-10-16: six tests passed. At that date each bank contained thirty questions; all sixty questions, corrections and references were displayed across both languages. Interactive mode was checked with one synthetic answer per language. Tests cover paired items, unique reproducible selection, full selection, invalid counts, unknown language and invalid references or identities.

## Work through an answer

Explain the case unaided, compare with the correction and reread the cited section. Privately record the distinction you missed and try a different example. No official certification readiness measure follows from the number of answers you consider correct.

## Limits

No network, external package, account or service cost. No personal data is recorded: the script does not write interactive answers to disk. Section existence is checked automatically; correction relevance still needs human review. No official syllabus, price, marking scheme, pass promise or protected content. See [NOTICE](../../NOTICE.md).

Added on 2026-10-19: three paired questions about the Lab 5 policy, type widening and runtime evidence. Each bank now has 33 items. Re-run the commands above for the current bank.
