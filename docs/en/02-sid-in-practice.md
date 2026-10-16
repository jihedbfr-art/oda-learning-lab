# Module 2 – SID in practice

[Version française](../fr/02-le-sid-en-pratique.md)

Unofficial community material, not affiliated with TM Forum. Prerequisite: [Module 1](01-etom-in-practice.md). Keep its hand-off exercise nearby.

## A shared meaning before a storage design

SID is TM Forum's Information Framework. Its public overview describes shared business definitions independent of a platform, programming language or protocol ([official page](https://www.tmforum.org/open-digital-architecture/information-framework-sid/), read 2026-10-16). This module uses that purpose to ask a practical question: when work changes hands, are both teams talking about the same thing?

An information model describes the meaning of business objects and their relationships. A data model makes implementation choices: tables or documents, keys, types and constraints. Agreeing that a purchase can need several technical setup steps does not decide how many database tables to create. SID is neither a database nor software to install.

## Product, service and resource

For this exercise, distinguish what someone bought, the capability delivered, and the means used to deliver it. These are teaching distinctions, not official SID class definitions.

| View | Question in our mobile-plan story | Invented exercise object |
|---|---|---|
| Customer | Who asked, and where should updates go? | Buyer note |
| Product | What did this person agree to receive? | Plan agreement |
| Service | What capability must work for them? | Connection promise |
| Resource | What technical means support that capability? | Assigned kit |

A SIM replacement changes the assigned kit. It need not create a new plan agreement. Keeping that distinction lets a support team explain why a technical change does not necessarily mean a new purchase.

## Worked example

Return to the synthetic order from Modules 0 and 1: choose a mobile plan, activate it, issue the first invoice, then investigate a data problem. Every object name below is invented for this exercise. The table is not a SID extract or a proposed standard message format.

| # | Hand-off | Objects crossing it | Meaning to preserve |
|---|---|---|---|
| 1 | Sales to order handling | Buyer note, plan agreement | The chosen plan and the buyer remain linked |
| 2 | Order handling to service setup | Setup slip linked to plan agreement | The requested capability follows the purchase |
| 3 | Service setup to technical allocation | Connection promise, kit request | Allocation serves this connection |
| 4 | Allocation back to service setup | Assigned kit linked to connection promise | The allocated means belong to the intended connection |
| 5 | Service setup to customer contact | Ready notice linked to plan agreement | A technical success becomes an understandable update |
| 6 | Usage collection to charging | Usage note, charge sheet | Consumption is attributed to the right agreement |
| 7 | Support to technical investigation | Trouble note, connection promise, assigned kit | Investigation follows the affected connection |

Give the plan agreement the invented reference `agreement-A`, then reuse it on the setup slip and ready notice. This exercise reference prevents confusion between two purchases; it is not an official attribute.

## Mistakes to avoid

- **Drawing tables too soon.** First explain each object to someone who does not maintain the database.
- **Using one word for several things.** “Line” might mean a purchase, a connection or a number. Ask which one changed.
- **Sending a whole record everywhere.** A receiving team needs the meaning and links relevant to its work, not every detail held upstream.
- **Treating an event as the object itself.** A ready notice reports a change; the agreement still exists after that notice is delivered.

## Exercise

Take the entities you listed at the end of Module 1. Rename them in everyday words and write one sentence explaining each. Draw a small model yourself: boxes for those objects, labelled links for their relationships.

Choose one hand-off. Mark who creates each object, who updates it and which reference joins the incoming and outgoing work. Then replace a SIM without changing the purchase. Explain which box changes and which links must survive. Finally, add a second order and show how you avoid mixing the two. No official UML model is needed.

## Check yourself

- How do product, service and resource differ in the SIM-replacement example?
- Which choices belong in the information model, and which belong in the implemented data model?
- What evidence would show that two teams attach the same meaning to a shared reference?

## Limits of this module

The full SID model and exact definitions are not reproduced here. The public overview lists v26.0; detailed suite pages were inaccessible during this check. See U1 in the [uncertainty register](../uncertainty-register.md) and the dated [source matrix](../../sources/source-matrix.md). This exercise supplies no official names, attributes, diagram or conformance evidence.
