# Module 4 – Open APIs in practice

[Version française](../fr/04-les-open-apis-en-pratique.md)

Unofficial community material, not affiliated with TM Forum. Prerequisites: [Module 2](02-sid-in-practice.md) and [Module 3](03-functional-framework-in-practice.md).

## A contract at the hand-off

The order desk and connection workshop from Module 3 need to exchange information. An interface contract sets out what a caller may request and how the receiving side represents its response. It is not the component that implements that behaviour. Two implementations can expose the same contract while using different storage and deployment choices.

TM Forum publishes an Open API programme and public definitions ([official overview](https://www.tmforum.org/oda/open-apis/), read 2026-10-16). We use five repositories to practise choosing an interface for a business interaction. This is an original mapping, not a prescribed implementation sequence.

## Five references, five different jobs

The numbers, titles and licences below were checked directly on 2026-10-16. Titles come from the linked definitions' metadata. Definitions and LICENSE files are pinned to repository commits so the evidence is reproducible; nothing from their schemas or example payloads is copied here.

| API | Title of linked definition | Proposed interaction | Repository licence |
|---|---|---|---|
| TMF620 | [Product Catalog Management](https://github.com/tmforum-apis/TMF620_ProductCatalog/blob/24e69f3026f2b514baa27d7206540fc7b55bcb45/TMF620-ProductCatalog-v4.1.0.swagger.json) | Consult what can be offered before choosing the plan | [Apache-2.0](https://github.com/tmforum-apis/TMF620_ProductCatalog/blob/24e69f3026f2b514baa27d7206540fc7b55bcb45/LICENSE) |
| TMF622 | [Product Ordering](https://github.com/tmforum-apis/TMF622_ProductOrder/blob/a3825f95248eb04fb1c7e2321305bc99631168a4/TMF622-ProductOrder-v4.0.0.swagger.json) | Submit and follow the purchase request | [Apache-2.0](https://github.com/tmforum-apis/TMF622_ProductOrder/blob/a3825f95248eb04fb1c7e2321305bc99631168a4/LICENSE) |
| TMF638 | [Service Inventory Management](https://github.com/tmforum-apis/TMF638_ServiceInventory/blob/50fc82942e423c81896362d1ab9847f7c918cf7f/TMF638-ServiceInventory-v4.0.0.swagger.json) | Inspect the service instances associated with delivery | [Apache-2.0](https://github.com/tmforum-apis/TMF638_ServiceInventory/blob/50fc82942e423c81896362d1ab9847f7c918cf7f/LICENSE) |
| TMF637 | [Product Inventory](https://github.com/tmforum-apis/TMF637_ProductInventory/blob/f598b4a02186071f2794b8f9b4f6904ef0a8aa52/TMF637-ProductInventory-v4.0.0.swagger.json) | Inspect the product instances held by the customer | [Apache-2.0](https://github.com/tmforum-apis/TMF637_ProductInventory/blob/f598b4a02186071f2794b8f9b4f6904ef0a8aa52/LICENSE) |
| TMF639 | [Resource Inventory Management](https://github.com/tmforum-apis/TMF639_ResourceInventory/blob/2693a854940de3c6e15b1aade24f981d94b75d3a/TMF639-ResourceInventory-v4.0.0.swagger.json) | Inspect the resources supporting the connection | [Apache-2.0](https://github.com/tmforum-apis/TMF639_ResourceInventory/blob/2693a854940de3c6e15b1aade24f981d94b75d3a/LICENSE) |

The selected definition versions are 4.1.0 for TMF620 and 4.0.0 for the other four. They are reading references, not a claim about the latest release or a recommendation to deploy them. Apache-2.0 was checked separately for every repository; it does not establish the licence of another repository or of the whole website. See U4 in the [uncertainty register](../uncertainty-register.md).

## Worked example

Return to the synthetic mobile-plan order. First the offer shelf consults a catalogue reference, TMF620, to explain what can be bought. The plan agreement from Module 2 records the choice; it is not itself a copy of that catalogue entry.

Next the order desk could use TMF622 to communicate the purchase request. Keep the reference that ties the request to the agreement. An acknowledgement is not evidence that the network is ready. Decide what later evidence the update desk needs before informing the buyer.

After delivery, an inventory view helps distinguish three questions. TMF637 concerns the product instance held by the customer; TMF638 concerns the service instance; TMF639 concerns supporting resources. In our invented vocabulary, these relate to the agreement, connection promise and assigned kit. This is a teaching comparison, not a field-by-field SID or API mapping.

If the customer replaces a SIM, ask which supporting resource changed and whether the purchase stayed the same. An inventory record is not a command to activate network equipment. The five references do not cover every technical interaction needed to deliver this story, and this module invents no missing activation endpoint.

## Mistakes to avoid

- **Calling the API the component.** The contract says what crosses a boundary; an implementation must do the work.
- **Confusing an offer with an owned product.** A catalogue describes possibilities; an inventory describes recorded instances.
- **Treating an accepted order as completed delivery.** Identify the evidence needed for readiness.
- **Combining definitions without checking versions.** Similar names do not establish compatible fields, operations or behaviour.

## Exercise

Use the hand-off and objects you chose in Module 2. Write a synthetic purchase request using your own invented fields. State who sends it, who receives it and what reference allows a later response to be matched to it. Do not use a real customer identifier or telephone number.

Then open the linked TMF622 definition. Privately compare your proposal with its selected version: which meanings align, which required information is missing, and which assumptions remain yours? Record differences in your own words, without copying a schema or example. Repeat the reasoning for a catalogue lookup, distinguishing the offer from the customer's eventual product instance. Your invented request is not a conformant payload.

## Check yourself

- Why does an API contract not determine the application's internal database?
- What is different between catalogue, product inventory and service inventory?
- Why do five accessible definitions and licences not establish a working integration?

## Limits of this module

No server, request, response or conformance test was executed. No authentication, version interoperability or operator deployment was assessed. Read the dated [source matrix](../../sources/source-matrix.md) alongside the pinned references. Choosing a contract is a design step; implementation and validation remain separate work.
