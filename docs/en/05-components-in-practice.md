# Module 5 – Components in practice

[Version française](../fr/05-les-composants-en-pratique.md)

Unofficial community material, not affiliated with TM Forum. Prerequisites: [Module 3](03-functional-framework-in-practice.md) and [Module 4](04-open-apis-in-practice.md). All names and contracts in the worked example are invented.

## Give responsibilities a boundary

Module 3 grouped work into responsibilities. Module 4 described contracts crossing a boundary. Now decide which responsibilities belong together and what their implementation promises to callers. A useful component description names the work it owns, the contract it exposes and the contracts it consumes. It should remain understandable before anyone chooses a language, database or deployment platform.

For our exercise, the order desk checks a setup request and preserves its link to the plan agreement. It does not allocate a SIM, announce network readiness or calculate a bill. This boundary gives the reviewer something to challenge: does the desk have enough information to accept the work, and who takes over afterward?

## What the public concept establishes

TM Forum's [component overview](https://www.tmforum.org/oda/implementation-architecture/components-canvas), read 2026-10-16, presents components as reusable software units that package logical functions and expose functionality through Open APIs. It also describes machine-readable definitions and execution on an ODA Canvas. These statements establish the published concept, not the status of our exercise.

The [public directory](https://www.tmforum.org/oda/directory/), read 2026-10-16, states that suppliers maintain their own functional mappings. A directory entry is therefore not evidence that our Python file passes a certification assessment. Exact requirements for an official component, the recommended manifest version and our example's mapping to an official component remain **to confirm**. U2 stays open in the [uncertainty register](../uncertainty-register.md). No official inventory, schema or diagram is reproduced here.

## Worked example

Continue the mobile-plan story. The offer shelf presents a possible purchase. The order desk receives a setup request referring to `agreement-A` and `offer-B`. These references are synthetic tokens, not customer identifiers. The request uses our own fields, `agreement` and `offer`; neither is asserted to be a standard attribute.

| Boundary | Invented responsibility or contract | Evidence in the lab |
|---|---|---|
| Owned work | Check a request and preserve its agreement reference | A validated request produces a prepared result |
| Exposed contract | `prepare` accepts two non-empty strings | Missing fields and incorrect types are rejected |
| Consumed contract | The offer shelf provides `read-offer` | Its dependency name must be declared |
| Output | Return the same agreement with state `prepared` | The success test compares both fields |

The dictionary returned by `describe()` announces this small design. `prepare()` enforces the request shape and checks the supplied dependency names. Its result means preparation only. There is no connection workshop behind it, and no claim that a subscriber can use mobile data.

The consumed operation is declared, not invoked. Passing the name `offer-shelf` proves neither that an offer exists nor that another implementation can be reached. An undeclared `charge-desk` is rejected before any result is returned. This makes a hidden dependency visible without adding a server or network call.

## Mistakes to avoid

- Treating one functional block as an automatic deployment boundary. Explain why its responsibilities should change together.
- Listing only exposed contracts. A caller needs to understand failures caused by consumed services too.
- Reading `prepared` as `active`. Each state needs a stated meaning and supporting evidence.
- Calling an invented description an official manifest. Readability and machine processing do not establish conformance.

## Exercise

Run [Lab 3](../../labs/03-component-contract/README.md). Predict the result when `agreement` is missing, when `offer` is a number and when the supplied dependencies include the charge desk. Then run the tests and compare the rejection points with your prediction.

On paper, add the connection workshop from Module 3. State what it receives, what it owns and what evidence would justify a ready notice. Decide how a failed preparation is reported without losing the agreement reference. Compare two possible boundaries with a colleague. Keep technology choices separate until you can explain ownership and failure handling.

## Check yourself

- Which responsibility is owned, exposed and consumed by the order desk?
- What does a declared dependency fail to prove about runtime behaviour?
- What additional evidence would justify telling the buyer that their connection works?

## Limits of this module

The lab is an original local contract exercise using only the Python standard library. It has no persistence, authentication, concurrency, runtime discovery or deployment. Passing tests establish only the stated input and dependency rules. They establish neither TM Forum conformance nor interoperability with a real system. Keep the dated sources above beside the [source matrix](../../sources/source-matrix.md) when reviewing the public concept.
