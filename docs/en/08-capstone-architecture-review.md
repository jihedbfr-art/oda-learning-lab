# Module 8 – Capstone architecture review

[Version française](../fr/08-projet-de-synthese.md)

Unofficial community material, not affiliated with TM Forum. Read Modules 1–7 first. All organisations, records and decisions below are invented.

## The fictional operator

The fictional operator in this exercise sells a mobile plan through a small offer shelf. Its order desk records the chosen offer and creates a plan agreement. A connection workshop asks a kit shelf for an assignment, then reports whether the requested connection works. An update desk tells the buyer what happened. Usage notes feed a charge desk, which prepares the first charge sheet. Later, mobile data fails. A fault desk opens a trouble note and asks the workshop to investigate the assigned kit. Restoration must be linked to the same agreement before the charge desk considers an adjustment. Messages can arrive twice, late or before their predecessors. The operator wants a review that exposes lost hand-offs without committing to a technology. Its review team has only synthetic records and local exercises. It must distinguish a proposed design from observed behaviour and identify evidence still missing before any operational decision.

## Ten review questions

Module links refer to our teaching examples. The expected evidence is a review deliverable, not a claim that it already exists.

| # | Question | Module | Expected evidence |
|---|---|---|---|
| 1 | Which flow and area own the failed hand-off? | [1](01-etom-in-practice.md) | Annotated journey |
| 2 | What changes when a SIM is replaced? | [2](02-sid-in-practice.md) | Object links before/after |
| 3 | Which reference survives from purchase to repair? | [2](02-sid-in-practice.md) | Linked synthetic records |
| 4 | Who decides readiness and who informs the buyer? | [3](03-functional-framework-in-practice.md) | Responsibility table |
| 5 | How does acceptance differ from completion? | [4](04-open-apis-in-practice.md) | Separate acknowledgement and readiness examples |
| 6 | Does an inventory entry command activation? | [4](04-open-apis-in-practice.md) | Stated boundary and missing interaction |
| 7 | What does the order component own and expose? | [5](05-components-in-practice.md) | Declaration and rejection evidence |
| 8 | Which consumed dependency remains untested? | [5](05-components-in-practice.md) | Dependency list and evidence gap |
| 9 | What prevents a duplicate adjustment effect? | [6](06-assurance-and-billing-in-practice.md) | Replay result and recovery gap |
| 10 | Who handles a missing predecessor or late review? | [6](06-assurance-and-billing-in-practice.md) | Pending-work trace and owner |

## Worked example

**Debatable proposal, not an official answer key.** These answers propose evidence and ownership; they do not record a deployed system.

1. Order preparation belongs to fulfilment, customer then service. The reported data failure crosses customer, service and resource work in assurance; the adjustment adds billing.
2. Change the assigned kit, retaining the plan agreement and connection promise. Compare the links before and after replacement.
3. Carry `agreement-A` through setup, readiness, trouble and adjustment records. Use a distinct incident reference to separate repairs concerning the same purchase.
4. The workshop decides technical readiness; the update desk communicates it. The fault desk owns investigation, while the charge desk owns the adjustment decision.
5. Accepting a setup request means preparation succeeded. Require separate restoration or readiness evidence before announcing a working connection.
6. An inventory entry describes a recorded instance. Leave network activation as an explicitly missing interaction rather than inventing an endpoint.
7. The order desk checks the request and retains its agreement. Its invented `prepare` contract rejects missing fields, wrong types and undeclared dependencies in Lab 3.
8. Declare `offer-shelf` and `read-offer`. Lab 3 checks dependency names only; offer existence and remote availability still need evidence.
9. Lab 4 demonstrates three invented credits instead of six with deduplication and ordering. Durable atomic adjustment and identity recording remain unproved after a crash.
10. Without restoration, leave adjustment and review pending. Assign investigation to the fault desk with the workshop. Flag a late review and process it when predecessors exist; lateness alone does not invalidate it.

## Mistakes to avoid

- Treating every responsibility as a separate application.
- Calling a proposed credit an entitlement or an actual invoice adjustment.
- Treating local replay as proof of durable processing.

## Exercise

Replace the SIM, then remove restoration from a disposable trace. Answer all ten questions with one evidence item each. Challenge the proposal by combining two responsibilities; explain the ownership tradeoff without changing the meaning of readiness.

## Check yourself

Mark each answer explained unaided, explained after rereading or still unclear. Identify one missing proof and its owner. Use [Module 7](07-preparing-for-certification.md) to organise revision; this module adds no certification facts.

## Limits of this module

No real case study, integration, deployment or TM Forum conformance assessment. Evidence from the labs remains local. Use the dated [source matrix](../../sources/source-matrix.md) and [uncertainty register](../uncertainty-register.md) for external claims; this proposal adds none and resolves no open question.
