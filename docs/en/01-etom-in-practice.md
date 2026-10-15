# Module 1 – eTOM in practice

[Version française](../fr/01-etom-en-pratique.md)

Unofficial community material, not affiliated with TM Forum. Prerequisite: [Module 0](00-discovering-oda.md). Sources and their limits are in the [source matrix](../../sources/source-matrix.md).

## What eTOM is, and what it is not

eTOM is TM Forum's Business Process Framework. It is a shared map of what a telecom business does, so that people from different companies can point at the same thing and mean the same thing. It is a way to classify and discuss processes.

It is not a workflow, it does not say in which order to do things, and it is not software. A billing platform can support some eTOM processes. It is not eTOM.

## Reading the map

The map is usually taught with two directions, which is what makes it useful.

- **Horizontal groupings** separate the business by what it works on. Going from the customer side towards the infrastructure side you find work centred on the customer, on the service the customer buys, on the resources that deliver it, and on the suppliers and partners involved.
- **End-to-end flows** cut across those groupings. Three are always taught: getting a product to a customer (fulfilment), keeping it working (assurance) and charging for it (billing).

A single business event therefore has two coordinates: which part of the business is acting, and which flow it belongs to.

> This is the widely taught top-level view. Exact names, numbering and the number of levels depend on the published version of the framework, and that version is not public in full. Do not quote a level number from this page. See U1 in the [uncertainty register](../uncertainty-register.md).

## Why the layers matter

Most real problems happen at a hand-off. The customer asks for a mobile plan. Someone must turn that into a service to configure, and someone else must turn that into resources to allocate. Each hand-off changes the vocabulary: customer order, then service order, then resource order. Naming the layer tells you who owns the next step, and where a failure is likely to hide.

## Worked example

The synthetic story from Module 0: a customer orders a mobile plan, the plan is activated, and the first invoice is issued.

| # | What happens | Business area acting | Flow |
|---|---|---|---|
| 1 | The customer chooses a plan and confirms | Customer | Fulfilment |
| 2 | The order is checked and split into what must be set up | Customer, then service | Fulfilment |
| 3 | The service is configured for this customer | Service | Fulfilment |
| 4 | A number and a SIM are allocated, and the network is told to activate the line | Resource | Fulfilment |
| 5 | The customer is told the line is live | Customer | Fulfilment |
| 6 | First usage is recorded and priced, and an invoice is issued | Customer, with usage from the resource side | Billing |
| 7 | The customer complains that mobile data does not work | Customer, then service, then resource | Assurance |

Notice that steps 2 and 6 touch two areas, and that step 7 goes down the layers and back up. That is normal: real events rarely sit in one box.

## Mistakes to avoid

- **Reading it as a sequence.** The flows describe families of work, not a fixed path.
- **Always going to the deepest level.** Start coarse. Refine only where a decision depends on it.
- **Confusing a process with a system.** "The billing system" is not a process. What the business does with it is.
- **Forcing one box per step.** If a step honestly spans two areas, write both and say why.

## Exercise

Use these eight synthetic events. For each one, write the area acting and the flow, with one sentence of justification in your own words.

1. A customer asks to move their line to another plan.
2. A field team replaces a faulty cabinet.
3. The operator buys a batch of SIM cards from a supplier.
4. A customer disputes an amount on an invoice.
5. A planned maintenance window is announced to affected customers.
6. A fraud pattern is detected on a group of lines.
7. A new offer is created and prepared for sale.
8. A customer asks to cancel their subscription.

Then:

- Find one event where two answers are defensible. Explain both and say which hand-off decides it.
- Pick one hand-off and write down which entities pass through it. You will reuse this list in Module 2 on the information model.

There is no official answer key here on purpose. The aim is to practise the reasoning, not to reproduce a reference mapping.

## Check yourself

- Why does an event have two coordinates?
- Which of the three flows is involved when a customer disputes a bill, and which when a service fails?
- Why is naming a hand-off more useful than naming a single process?

## Limits of this module

It teaches how to read and use the framework. It copies no official diagram or label list and states no framework version. The first level of detail you add to your own mapping should be checked against the official framework page before you publish it.
