# Labs

[Version française](README.fr.md)

Lab 1 is documented; Labs 2 and 3 remain planned. The guide distinguishes executed tests from the interactive session, which was not run.

All labs run locally, use synthetic data only, need no paid service, and make no claim of TM Forum conformance.

| Lab | Goal | Starting point | State |
|---|---|---|---|
| 1. Number portability as a process | Follow a multi-operator process with timeouts and compensation, then map each step to the Module 0 pieces | The existing public repository [`bpmn-provisioning-patterns`](https://github.com/jihedbfr-art/bpmn-provisioning-patterns) (Camunda, Spring Boot, Kafka) | [Documented](01-number-portability/README.md) |
| 2. A small product catalogue | Build a tiny catalogue API on synthetic data and compare its shape with a public Open API specification | A public specification from `tmforum-apis`, after checking its licence | Planned |
| 3. A component on a local Canvas | Describe a "hello" component with a `v1` manifest and run it on a local Kubernetes cluster | The public `tmforum-oda/oda-canvas` reference implementation | Planned; heavy, so scheduled rather than run on every push |

Each lab will state its prerequisites, the commands, the assertions that must pass, its limits and its running cost.
