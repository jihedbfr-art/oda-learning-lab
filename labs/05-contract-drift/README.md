# Lab 5 – Contract drift

[Version française](README.fr.md)

Continue [Module 5](../../docs/en/05-components-in-practice.md#compare-two-declarations) and [Lab 3](../03-component-contract/README.md). The order desk publishes two invented declarations. Compare what they promise before deciding what a caller would need to revisit. All data and rules below belong to this exercise; no official schema is reproduced.

## Run

Python 3.9 or later and its standard library are sufficient. From the repository root:

```console
python -X utf8 labs/05-contract-drift/drift.py
python -X utf8 labs/05-contract-drift/drift.py labs/05-contract-drift/drift_samples.json
python -m unittest discover -s labs/05-contract-drift -p test_drift.py
python tools/check_docs.py
```

The default file is found beside the script, even from another working directory. A supplied path is relative to your current directory. `-X utf8` keeps redirected bilingual output in UTF-8, including on Windows. The script prints both languages together; operation and field names stay unchanged.

The sample produces six findings: one compatible addition, two changes to review and three breaks. Exit 0 means comparison completed, even when a break is reported. Invalid input or an unreadable file produces a bilingual error on stderr and exit 2. An empty comparison says that no declared change was found; it does not claim compatibility at runtime.

## Read the declaration

[drift_samples.json](drift_samples.json) contains exactly `before` and `after`. Each declaration is either `{}` or an object with `exposes`, a mapping of operation names. Each operation contains exactly `fields`, a mapping of field names to `type` and a Boolean `required`. Empty `exposes` and empty `fields` are allowed. Unknown keys, blank names and invalid shapes are rejected rather than silently ignored.

This is a separate teaching format inspired by Lab 3, not a parser for `describe()` or a complete component description. It describes flat request fields only. It contains no returned fields, dependency declarations or runtime observations. Adding those keys is an input error.

Types are the invented vocabulary `string`, `integer`, `number`, `boolean`, `null`, `array` and `object`. A non-empty list represents alternatives, for example `["string", "null"]`. Unknown types and duplicate alternatives are rejected. `number` includes `integer` in this exercise; no other containment is inferred. List order does not matter, and `number` is equivalent to `["integer", "number"]`. Array items and object properties are not described.

## Classification rules

Comparison goes from the old declaration to the new one. These are review rules for this lab, not a universal compatibility policy.

| Declared change | Classification | Reading |
|---|---|---|
| Optional field added | compatible | The new declaration does not require the caller to provide it |
| Required field added or optional field made required | review | Identify callers that may omit it before deciding how to migrate |
| Required field made optional | compatible | The declaration accepts omission |
| Type widened to a strict superset | review | Inspect the meaning of newly accepted values |
| Type changed or narrowed | breaking | Previously accepted values can be excluded |
| Required field removed | breaking | The lab treats removal of a promised required field as a break |
| Optional field removed | review | Check whether callers still send or rely on it |
| Operation removed | breaking | Callers lose an operation |
| Operation added | compatible | Existing operations remain available in the declaration |

A `string` becoming `["string", "null"]`, or an `integer` becoming `number`, is widening. A `string` becoming `integer`, or `number` becoming `integer`, is a breaking change under these rules. Review does not mean safe: making a field required may already break a caller, so a person must examine the usage.

Each finding has a stable `code`, a `classification`, a path represented as a list of keys, and `message.en` / `message.fr`. Operations and fields are visited in sorted order. An added or removed operation is reported once at its boundary, without redundant findings for its fields. A retained field whose type and requiredness both change produces two findings. Equivalent type declarations produce none. `compare(before, after)` returns a list and leaves its arguments untouched.

## Try and explain

1. Predict the six findings before running the sample. Locate each changed key in the two declarations.
2. In a disposable copy, change `quantity` back to `integer`. The widening finding should disappear.
3. Make `comment` required. Explain why it now needs review rather than declaring the caller safe.
4. Give a field the type `mystery`. The whole comparison must fail, including if its operation was added or removed.
5. Keep both declarations identical but imagine that the implementation applies an adjustment twice. Explain why this comparison sees no change, then use [Lab 4](../04-event-trace/README.md) to reason about observable effects.

## What the comparison cannot see

A declaration can remain unchanged while the code stops enforcing it. The script neither invokes operations nor tests responses, persistence, concurrency, authentication, timing, event ordering or idempotence. It cannot prove that a dependency exists, that a repair completed, or that an adjustment was applied once. [Module 6](../../docs/en/06-assurance-and-billing-in-practice.md) keeps those evidence gaps separate from the declared contract.

The 17 tests cover empty and unchanged declarations, all classification rules, type equivalence, multiple changes on one field, input validation, unknown types, unchanged inputs and the CLI. They establish this local exercise’s behaviour only. No real customer data, network call, deployment, conformance or certification assessment. See the [notice](../../NOTICE.md).
