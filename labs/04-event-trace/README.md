# Lab 4 – An event trace

[Version française](README.fr.md)

Continue [Module 6](../../docs/en/06-assurance-and-billing-in-practice.md). Synthetic data only, with no TM Forum conformance claim or real system.

## Run

Standard Python 3, no network or external package. From the repository root:

```console
python labs/04-event-trace/event_trace.py
python -m unittest discover -s labs/04-event-trace -p test_trace.py
python tools/check_docs.py
```

Executed on 2026-10-16: ten tests passed. The naive mode produces 6 invented credits; the idempotent, ordered mode produces 3. Both identify duplicate `credit-A`, out-of-order `restore-A` and late `review-A`. Output labels are EN/FR; event tokens are not translated.

## Read the file

[events.json](events.json) is read beside the script, even from another working directory. File order represents deliveries. `sequence` is the invented business order for one incident; `occurred` and `received` are integer logical ticks, not real timestamps. Delay strictly above ten ticks is flagged. Duplicate identity stays stable; only receipt may change.

The naive mode sums amounts in supplied order without enforcing business transitions. The ordered mode requires opening, restoration, adjustment and review, deduplicates by identity and waits for missing sequences. Conflicting identities and sequences shared by different events are rejected. Gaps appear in `pending`. Structural validation remains active in both modes.

## Try and explain

1. Predict both totals before running.
2. Remove restoration from a copy. Sequences 3 and 4 remain pending, with no credit.
3. In a Python call, compare `replay(events)` with `replay(events + events)`: ordered treatment retains one effect.
4. Change the duplicate amount: the conflict must be rejected.
5. Explain which Module 6 owner handles the gap and how to prove the billing hand-off.

## Limits

Ten tests cover duplication, disorder, lateness, replay, gaps, conflicts, structure, duplicate sequences and mutation isolation. Memory starts fresh on every call: no durable deduplication, transaction, network failure, persistence, security or exactly-once delivery is demonstrated. One incident and agreement per trace. No real currency or service cost. An incomplete trace returns pending work without claiming completion; invalid input prints a bilingual error and returns 1. See [NOTICE](../../NOTICE.md).
