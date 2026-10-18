# Study-path glossary

[Version française](../fr/glossary-termes.md) · [Beginner FAQ](faq-beginners.md)

These 30 explanations use our modules’ own examples, not official definitions or labels. Read the linked section for the reasoning behind each term.

The [source matrix](../../sources/source-matrix.md) records dated external evidence; the [uncertainty register](../uncertainty-register.md) records its limits. U1 remains partial and U5 remains partial: this glossary states neither a current SID version nor a status for TAM.

## 1. Process

Work the business needs to carry out, such as checking an order. Naming that work helps us discuss it without choosing the software that will perform it.

[Module 1: What eTOM is, and what it is not](01-etom-in-practice.md#what-etom-is-and-what-it-is-not)

## 2. Business area

The part of the business concerned by a step in our story. A request can cross customer, service and resource work, so one step may involve several areas.

[Module 1: Reading the map](01-etom-in-practice.md#reading-the-map)

## 3. Flow

A way to follow related work across business areas, such as delivery or repair. In these modules it groups work by purpose rather than prescribing a fixed execution order.

[Module 1: Reading the map](01-etom-in-practice.md#reading-the-map)

## 4. Fulfilment

The delivery side of our mobile-plan story, from the buyer’s choice to a working connection. Checking the order and assigning a SIM contribute to it from different business areas.

[Module 1: Worked example](01-etom-in-practice.md#worked-example)

## 5. Assurance

The work used here to investigate a service problem and restore the expected capability. The data-failure example moves from the customer’s complaint to service and resource investigation.

[Module 1: Worked example](01-etom-in-practice.md#worked-example)

## 6. Billing

The work that connects recorded consumption to an amount charged in our example. A technical repair does not by itself decide a financial adjustment.

[Module 1: Worked example](01-etom-in-practice.md#worked-example)

## 7. Hand-off

The point where one responsibility passes work to another. We check both who takes over and which information must keep its meaning across that boundary.

[Module 1: Why the layers matter](01-etom-in-practice.md#why-the-layers-matter)

## 8. Business object

Something the teams need to talk about and recognise, such as a plan agreement. Its meaning and relationships come before a choice of database table or document.

[Module 2: A shared meaning before a storage design](02-sid-in-practice.md#a-shared-meaning-before-a-storage-design)

## 9. Information model

A description of what our objects mean and how they relate. It can explain why several setup steps belong to one purchase without deciding how to store them.

[Module 2: A shared meaning before a storage design](02-sid-in-practice.md#a-shared-meaning-before-a-storage-design)

## 10. Data model

The storage choices that put information into an implementation. Tables, keys and constraints answer different questions from the meaning of a purchase or connection.

[Module 2: A shared meaning before a storage design](02-sid-in-practice.md#a-shared-meaning-before-a-storage-design)

## 11. Product

In our exercise, the view of what the buyer agreed to receive. We use the invented plan agreement to keep that purchase distinct from the technical means behind it.

[Module 2: Product, service and resource](02-sid-in-practice.md#product-service-and-resource)

## 12. Service

In our exercise, the capability that must work for the buyer. The connection promise describes that need without equating it with a particular SIM.

[Module 2: Product, service and resource](02-sid-in-practice.md#product-service-and-resource)

## 13. Resource

In our exercise, a technical means used to deliver the capability. Replacing the assigned SIM changes that means without necessarily changing the purchase.

[Module 2: Product, service and resource](02-sid-in-practice.md#product-service-and-resource)

## 14. Reference

A value that lets us recognise the same object across several steps. Our invented agreement-A links preparation and readiness to one purchase; it is not an official field.

[Module 2: Worked example](02-sid-in-practice.md#worked-example)

## 15. Functional block

A grouping of responsibilities used to discuss who handles the work. Our order desk is such a block, but drawing it does not require a separate deployed application.

[Module 3: Three views of the same hand-off](03-functional-framework-in-practice.md#three-views-of-the-same-hand-off)

## 16. Decision owner

The responsibility that decides whether an outcome can be announced. In our story the connection workshop decides technical readiness, while the update desk communicates it.

[Module 3: Worked example](03-functional-framework-in-practice.md#worked-example)

## 17. Interface contract

An agreement about what a caller can request and what response it can expect. It describes the exchange, leaving the receiving implementation’s storage choices separate.

[Module 4: A contract at the hand-off](04-open-apis-in-practice.md#a-contract-at-the-hand-off)

## 18. Implementation

The software that actually carries out the behaviour described by a contract. Two implementations may offer the same exchange while organising their internal work differently.

[Module 4: A contract at the hand-off](04-open-apis-in-practice.md#a-contract-at-the-hand-off)

## 19. Catalogue

The view of what could be offered to a buyer in our example. Choosing an offer is different from recording the product that the buyer eventually holds.

[Module 4: Mistakes to avoid](04-open-apis-in-practice.md#mistakes-to-avoid)

## 20. Inventory

The view of recorded instances, such as a service or an assigned resource. Reading a record does not itself activate equipment or prove the connection works.

[Module 4: Worked example](04-open-apis-in-practice.md#worked-example)

## 21. Acknowledgement

A response telling the caller that its request has been received or accepted in the exchange being designed. Our example still needs separate readiness evidence before telling the buyer the connection works.

[Module 4: Worked example](04-open-apis-in-practice.md#worked-example)

## 22. Component

A software boundary around work that belongs together in our design. We describe what the order desk owns, exposes and consumes before choosing how to deploy it.

[Module 5: Give responsibilities a boundary](05-components-in-practice.md#give-responsibilities-a-boundary)

## 23. Exposed contract

The operation a component makes available to its callers. Our invented prepare operation checks the request and returns a prepared result, not an active connection.

[Module 5: Worked example](05-components-in-practice.md#worked-example)

## 24. Consumed dependency

Another contract that a component declares it needs. Lab 3 checks the dependency name but never calls the remote service, so the declaration does not prove availability.

[Module 5: Worked example](05-components-in-practice.md#worked-example)

## 25. Event identity

The value used to recognise repeated deliveries of one event. It differs from an agreement reference because several legitimate events can concern the same purchase.

[Module 6: Three ways a relay can fail](06-assurance-and-billing-in-practice.md#three-ways-a-relay-can-fail)

## 26. Idempotence

Here, replaying the same adjustment keeps a single financial effect. Lab 4 demonstrates this within one call; restarting a process does not preserve its memory.

[Module 6: Worked example](06-assurance-and-billing-in-practice.md#worked-example)

## 27. Deduplication

Recognising that an event has already been handled so its effect is not applied again. This check alone cannot put an early adjustment after the restoration it depends on.

[Module 6: Three ways a relay can fail](06-assurance-and-billing-in-practice.md#three-ways-a-relay-can-fail)

## 28. Out-of-order event

An event received before a predecessor required by our sequence. The exercise keeps the adjustment pending until restoration arrives instead of treating the missing step as success.

[Module 6: Three ways a relay can fail](06-assurance-and-billing-in-practice.md#three-ways-a-relay-can-fail)

## 29. Late event

An event received long after it occurred, according to the exercise’s chosen threshold. It is flagged but can still be processed once its predecessors are present.

[Module 6: Three ways a relay can fail](06-assurance-and-billing-in-practice.md#three-ways-a-relay-can-fail)

## 30. Evidence

An observation or deliverable that supports a specific statement in the review. A local replay result supports a claim about that run, not a claim about a deployed operator system.

[Module 8: Ten review questions](08-capstone-architecture-review.md#ten-review-questions)
