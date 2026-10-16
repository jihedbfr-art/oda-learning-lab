# Module 6 – Assurance and billing in practice

[Version française](../fr/06-assurance-et-facturation-en-pratique.md)

Unofficial community material, not affiliated with TM Forum. Prerequisites: [Module 2](02-sid-in-practice.md), [Module 3](03-functional-framework-in-practice.md), [Module 4](04-open-apis-in-practice.md) and [Module 5](05-components-in-practice.md). This is an invented continuation of the mobile-plan story, not an operator case study.

## Follow the evidence beyond restoration

The buyer's mobile data stops working after activation. Support records a trouble note linked to the connection promise. The connection workshop investigates the assigned kit, restores the connection and sends evidence back. The charge desk then proposes an adjustment to the charge sheet. Repairing the connection and adjusting the bill are separate decisions with separate owners.

In this exercise the adjustment is three invented credits. This is neither a tariff nor a compensation entitlement. A real policy, approval process and accounting treatment would need separate evidence; none is inferred from a technical restoration.

## Keep objects, blocks and contracts together

| Hand-off | Objects from Module 2 | Blocks from Module 3 | Invented contract and owner |
|---|---|---|---|
| Report failure | Trouble note, plan agreement | Fault desk | Record the affected agreement; fault desk owns investigation |
| Investigate | Connection promise, assigned kit | Connection workshop, kit shelf | Return diagnosis linked to the same incident |
| Restore | Connection promise, trouble note | Connection workshop, update desk | Report restoration evidence; workshop owns technical readiness |
| Adjust | Charge sheet, plan agreement, trouble note | Charge desk | Apply one approved adjustment; charge desk owns the amount |
| Review | Adjustment record, trouble note | Fault desk, charge desk | Confirm the trace is complete before closing review |

These are our own teaching objects and contracts. Module 4's distinction between a contract and its implementation still matters. Module 5 adds the need to declare dependencies: the charge desk cannot silently rely on a restoration signal that nobody promises to deliver. Keep an incident reference and agreement reference across every hand-off.

## Three ways a relay can fail

A duplicate adjustment message can apply the same credit twice. The consumer needs a stable event identity and must reject conflicting content under that identity. Deduplication in a local list is useful here, but durable processing would also need a decision about atomic writes and recovery after a crash.

An out-of-order message arrives before a predecessor. In [Lab 4](../../labs/04-event-trace/README.md), the adjustment arrives before restoration. The ordered treatment buffers it until sequence two arrives. Waiting preserves the dependency; deduplication alone would not. If restoration never arrives, the gap remains visible rather than being treated as success.

A late message has a large gap between occurrence and receipt. Our invented threshold is ten logical ticks. Review arrives thirteen ticks after it occurred. It is flagged and processed once its predecessors are present. This teaching rule does not prescribe an operational SLA. Receipt order, sequence order and occurrence time answer different questions.

## Worked example

Read the five records in the lab JSON in file order. Opening has sequence one. Adjustment has sequence three, restoration sequence two, then adjustment is delivered again. Review has sequence four and arrives late. The naive path blindly sums both adjustment deliveries: six credits. The idempotent, ordered path produces three credits and records opening, restoration, adjustment and review in sequence order.

Replay the full list twice in one call. The ordered treatment keeps one financial effect. Start a fresh process and its memory starts empty: this lab is not a durable deduplication service. Remove restoration and sequences three and four remain pending, with no adjustment applied.

## Mistakes to avoid

- Closing the trouble note as soon as a technical repair is reported, without checking the remaining financial hand-off.
- Using the agreement reference as the event identity: several legitimate events can concern one agreement.
- Suppressing every late message: lateness does not establish that the business fact is false.
- Claiming exactly-once delivery because a local replay gives the expected total.

## Exercise

Run both modes, explain each diagnostic and remove the restoration record in a disposable copy. Name the owner who should investigate the missing event. Then describe a crash between writing an adjustment and remembering its event identity. What must be made atomic in a durable implementation?

## Check yourself

- Which objects link a repair to the purchase and the charge sheet?
- Why do deduplication and ordering solve different problems?
- What evidence is still missing when the gap list is empty?

## Limits of this module

No real billing, customer data or network integration. The sequence and adjustment rules are invented for one incident per trace. No official event schema, TM Forum conformance or operational service level is claimed. Framework claims remain scoped to the dated [source matrix](../../sources/source-matrix.md); this worked example introduces no new claim about a third party.
