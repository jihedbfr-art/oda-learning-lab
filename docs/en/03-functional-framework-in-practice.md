# Module 3 – Functional Framework in practice

[Version française](../fr/03-le-functional-framework-en-pratique.md)

Unofficial community material, not affiliated with TM Forum. Prerequisites: [Module 1](01-etom-in-practice.md) and [Module 2](02-sid-in-practice.md).

## Give the work a functional home

A process describes the work to be done. An information model explains the objects involved. A functional view asks what responsibilities the software must provide to handle those objects. TM Forum describes its Functional Framework as a shared systems view of activities and related functions ([official overview](https://www.tmforum.org/oda/information-systems/functional-framework/), read 2026-10-16).

We will practise that distinction using our mobile-plan story. Every block below has an invented everyday name. None is an official framework label or a prescribed application boundary.

## Three views of the same hand-off

| View | Question | Our order example |
|---|---|---|
| Process, from Module 1 | What work happens, in which business area and flow? | Check the requested change; customer then service, fulfilment |
| Information, from Module 2 | Which objects retain their meaning across the hand-off? | Plan agreement and setup slip |
| Function, in this exercise | What responsibility handles that information? | The order desk prepares work for the connection workshop |

A functional block is not necessarily a deployable component. Applications may combine or share responsibilities, with clear ownership rules. A box does not settle that design.

## Worked example

Keep the same synthetic sequence: a customer chooses a mobile plan, receives a working connection and a first invoice, then reports a data problem. Carry the invented objects from Module 2 across the steps.

| # | Process step and business area | Objects handled | Invented functional block |
|---|---|---|---|
| 1 | Choose and confirm; customer | Buyer note, plan agreement | Offer shelf and order desk |
| 2 | Check and prepare; customer then service | Plan agreement, setup slip | Order desk |
| 3 | Set up the connection; service | Setup slip, connection promise | Connection workshop |
| 4 | Allocate means; resource | Kit request, assigned kit | Kit shelf |
| 5 | Announce readiness; customer | Ready notice, plan agreement | Update desk |
| 6 | Record usage and charge; customer with resource input | Usage note, charge sheet | Charge desk |
| 7 | Investigate a data problem; customer, service, resource | Trouble note, connection promise, assigned kit | Fault desk, connection workshop and kit shelf |

Rows 1–5 belong to fulfilment, row 6 to billing and row 7 to assurance, following Module 1's teaching example. The same connection workshop helps delivery and investigation. A flow therefore does not need its own copy of every function.

Suppose the kit shelf allocates a replacement SIM while the original plan agreement remains in force. The connection workshop must receive the new assignment before the update desk announces success. Who owns readiness, which link identifies the connection, and what if the update arrives first? These questions expose missing responsibilities.

## Where TAM fits

The checked source matrix and U5 record that TM Forum presents the Functional Framework as an evolution of the now legacy Application Framework (TAM), on the overview cited above. That establishes the public relationship only. A complete migration mapping or the withdrawal of every TAM document remains to confirm; neither is inferred here.

## Mistakes to avoid

- **Turning every step into an application.** Several steps can use the same function.
- **Confusing a business area with a block.** “Resource” names a view of the work; our kit shelf names a responsibility in the example.
- **Duplicating functions for each flow.** First check whether the information and decision are actually different.
- **Assigning technology too early.** Explain who owns the decision before choosing a product or deployment shape.

## Exercise

Take your hand-off and object list from Modules 1 and 2. Group the work into blocks with names you can explain without a glossary. For each block, write its input, output and decision owner. Keep the process area and flow beside it.

Now add the replacement-SIM case. Reuse a block where its responsibility is unchanged. Mark one failure at a boundary and explain who detects it, who recovers and which object links the recovery to the purchase. Compare two possible groupings and defend your choice. There is no official answer key.

## Check yourself

- Why can one function support both fulfilment and assurance?
- What is missing if a block has an input and output but no decision owner?
- Why does a functional drawing not determine a deployable component?

## Limits of this module

This is an original reasoning exercise, not a reproduced function map, version claim or conformance assessment. Consult the [source matrix](../../sources/source-matrix.md) and [uncertainty register](../uncertainty-register.md), particularly U5. Component boundaries and interface contracts need separate design work; the table does not decide them.
