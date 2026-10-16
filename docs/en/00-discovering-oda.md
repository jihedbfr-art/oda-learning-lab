# Module 0 – Discovering ODA

[Version française](../fr/00-decouvrir-l-oda.md)

Unofficial community material, not affiliated with TM Forum. Sources and their limits are listed in the [source matrix](../../sources/source-matrix.md).

## The idea in one paragraph

A telecom operator runs a lot of IT: ordering, billing, catalogue, network activation, incident handling. For years each of those was a separate, tightly coupled system. The Open Digital Architecture, or ODA, is TM Forum's answer: describe the business in a shared vocabulary, split the software into components with standard interfaces, and run them on a common platform. It is a blueprint, not a product you install.

## Five pieces to keep apart

| Piece | The question it answers | One-line picture |
|---|---|---|
| Business Process Framework (eTOM) | What does the operator do, end to end? | A map of business processes |
| Information Framework (SID) | What things does the business talk about? | A shared vocabulary: customer, product, service, resource |
| Functional Framework | Which functions group together? | Building blocks for applications; its relationship to the Application Framework (TAM) is still to confirm (U5) |
| Open APIs | How do systems talk to each other? | Standard REST interfaces for business functions |
| ODA Components and Canvas | How is it built and run? | Deployable components, and the runtime that hosts them |

Mixing these up is the most common beginner mistake. eTOM is about processes, SID about data, and neither is software.

## What can be checked today

Some of the above can be inspected directly in public repositories, which makes it concrete.

- The runtime is open source. The Canvas reference implementation lives at `tmforum-oda/oda-canvas`, licensed Apache-2.0. On 15 October 2026 its latest releases were in the 1.2 line, with a 1.2.6 release candidate dated 14 October.
- A component is described by a manifest. The Canvas definition of that manifest currently carries four versions: `v1beta2`, `v1beta3`, `v1beta4` and `v1`. No recommended version is established (U2 is open), and some guideline pages still describe `v1beta2`.
- The standard APIs are published in a separate public organisation, `tmforum-apis`, which held 97 repositories on the same date. The licence is stated per repository, so check it before reusing a file.

## Exercise

Take this synthetic story: a customer orders a mobile plan, the plan is activated, and the first invoice is issued.

1. List the business steps in your own words. This is the eTOM side.
2. List the things the steps handle: customer, order, plan, line. This is the SID side.
3. For each step, name the system that would act and the interface it would call. This is the Open API and component side.
4. Decide which of your components would run on a Canvas, and which would stay outside.

There is no single correct answer. Compare your split with someone else's and explain the differences.

## Check yourself

- Can you say why eTOM and SID are not software?
- Can you explain the difference between a component and the platform that runs it?
- Why is a lab that runs locally not proof of conformance?

## Limits of this module

It explains concepts, it does not reproduce any official text. The complete eTOM and SID models are not public. A SID version number is shown on the public overview page, while the eTOM one is still to confirm; the current state is tracked in the [uncertainty register](../uncertainty-register.md).
