# Lab 1 – Number portability as a process

[Version française](README.fr.md)

Unofficial community lab. Prerequisite: [Module 1 – eTOM in practice](../../docs/en/01-etom-in-practice.md). Use synthetic data only. Nothing here certifies TM Forum conformance.

## Sources and prerequisites

This guide reads the public [upstream README](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/README.md), [process model](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/src/main/resources/processes/number-portability-saga.bpmn) and [build configuration](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/pom.xml) at revision `9d1bf041bdf051586ba1edfda320649b925d2e5a`, consulted 2026-10-16. The exercise mapping below is our own interpretation.

For the Docker route, have Git, Docker with Compose, and local ports 8080, 9092, 16686 and 4318 available. The Maven route needs Java 17 and Maven, as declared by the build and used by the README. Container downloads, storage and compute use local resources; no paid cloud service is needed. Download sizes and resource requirements have not been measured.

## Obtain and start the lab

Use the upstream repository's **Code** menu to obtain a local clone, then enter its root folder. Its README supplies no clone command, so this guide does not invent one. Check the revision if you want the exact files linked above.

These are the exact setup commands from its Quick start, for a Bash-compatible shell:

```bash
cp .env.example .env
docker compose up -d
```

Open Cockpit at `http://localhost:8080/camunda` and Jaeger at `http://localhost:16686`. See upstream for local development access settings; do not use customer or production credentials. The README also provides this alternative:

```bash
mvn spring-boot:run
```

That alternative uses an in-memory database and loses state on restart. It does not start Kafka for you. Read the upstream Running it section before choosing it; do not assume it validates broker delivery.

For starting a request and sending a donor decision, follow the exact HTTP examples in [Quick start](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/README.md#quick-start). Keep them on localhost with synthetic fixtures. Record the returned request reference and substitute it for the response URL placeholder; leaving the placeholder literal does not target your instance. No message should reach a real operator.

## Trace the process before classifying it

Follow the model's activity IDs, rather than guessing an order from the business framework:

1. `validateRequest` checks the request, then `notifyDonor` requests donor notification.
2. `awaitDonorResponse` contains the waiting message event. Its interrupting `slaTimeout` boundary timer exits the wait if no response arrives in time.
3. An accepted decision passes through `activateOnRecipient`, `notifyCompletion`, then the `completed` end event.
4. A rejected decision and a timeout both reach `compensateProvisioning`, then the human task `manualReview`. The `rejected` end event comes **after** that task is completed, not merely after compensation.

Start with acceptance. Repeat with rejection, then with no response. For each case, record the current activity, the request reference and the evidence you observed. Read the configured timeout instead of treating it as a regulatory deadline. No jurisdiction-specific SLA is established here.

## Your mapping

Before reading the example, fill one row per activity: **process step → business area acting → flow (fulfilment / assurance / billing)**. Add the incoming object, outgoing object and one sentence explaining your choice. Use the coarse business areas from Module 1; do not invent official eTOM codes.

### Example of a possible answer

This is a debatable proposal, not an official answer key. The grouping describes responsibility in the story, not the name of a software component.

| Process step | Business area acting | Flow | Reasoning |
|---|---|---|---|
| Validate request | Customer | Fulfilment | Check the requested change before arranging delivery |
| Notify donor | Service, then partner | Fulfilment | Ask another operator to coordinate that change |
| Await response / SLA timeout | Partner and service | Fulfilment | Await a prerequisite for completing the request |
| Activate on recipient | Service / resource | Fulfilment | Represent the technical delivery step |
| Notify completion | Customer | Fulfilment | Report the outcome of the requested change |
| Compensation | Service / resource | Fulfilment | Recover from an unsuccessful fulfilment attempt |
| Manual review | Customer / partner | Fulfilment; assurance defensible if handling a service incident | A person examines why the request could not complete |

A timer is not automatically assurance. Here it controls an unfinished fulfilment request. Billing is not demonstrated by this process; leave it absent rather than forcing every flow into the table.

## Objects crossing the hand-offs

Trace customer intake → orchestration → donor boundary → recipient step → customer update. Use invented names such as “move note”, “donor answer” and “outcome notice”. Link them with the same request reference. These are exercise objects, not SID classes or standard payloads.

At each hand-off ask: who owns the next action, what information must survive, and what evidence proves receipt? Distinguish a notification requested from one actually delivered. Save your object list for the information-model exercise in Module 2. Draw the relationships yourself and explain how a late donor answer could be distinguished from a current one.

## Checks and limits

The upstream README documents these test commands:

```bash
mvn test       # process tests against the embedded H2 engine — no Docker
mvn verify     # also runs the Testcontainers check against a real Kafka broker and a PostgreSQL database
```

Local check on 2026-10-16 at the revision above: `mvn test` passed, 12 tests, no failures, errors or skips (including all four portability paths). Only embedded tests were executed; the interactive Docker/Cockpit lab was not started. `mvn verify` and Testcontainers integrations were not executed.

The embedded process tests check acceptance, rejection, timeout and invalid input. They use a mocked event publisher; the timeout test advances the engine clock and triggers its timer job. This is not a wall-clock or broker-delivery measurement.

The lab demonstrates an executable process with a timeout and a compensation branch at the tested scope. Its [activation delegate](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/src/main/java/com/jihedapps/provisioning/delegate/ActivateOnRecipientDelegate.java) and [compensation delegate](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/src/main/java/com/jihedapps/provisioning/delegate/CompensateProvisioningDelegate.java), read 2026-10-16, publish events; they do not activate or undo a real network configuration. Compensation is a service task here, not proof of BPMN compensation-event semantics.

It demonstrates no TM Forum conformance, standard Open API, real inter-operator integration, regulatory compliance or testing on real customer data. Keep your own execution log separate from this mapping proposal.
