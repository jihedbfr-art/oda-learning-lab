# oda-learning-lab

[🇫🇷 Lire en français](README.fr.md)

Unofficial community material for learning TM Forum's Open Digital Architecture (ODA): short bilingual modules, runnable labs on synthetic data, and a public record of what is verified and what is not.

> **Not affiliated with, endorsed by or certified by TM Forum.** "TM Forum", "eTOM" and "ODA" are names owned by their holders and appear here only to describe the subject. Nothing in this repository replaces official TM Forum courses, specifications or certification. See [NOTICE.md](NOTICE.md).

## Why this exists

ODA is documented mostly for members, in English, and spread over many pages. This repository is a French/English study path written from scratch, grounded in public sources, with the sources and their limits written next to every claim.

## What is here today

| Area | State |
|---|---|
| [Module 0 – Discovering ODA](docs/en/00-discovering-oda.md) | Draft, written |
| [Module 1 – eTOM in practice](docs/en/01-etom-in-practice.md) | Draft, written |
| [Module 2 – SID in practice](docs/en/02-sid-in-practice.md) | Draft, written |
| [Module 3 – Functional Framework in practice](docs/en/03-functional-framework-in-practice.md) | Draft, written |
| [Module 4 – Open APIs in practice](docs/en/04-open-apis-in-practice.md) | Draft, written |
| [Module 5 – Components in practice](docs/en/05-components-in-practice.md) | Draft, written |
| [Module 6 – Assurance and billing in practice](docs/en/06-assurance-and-billing-in-practice.md) | Draft, written |
| [Module 7 – Preparing for certification](docs/en/07-preparing-for-certification.md) | Draft, written; 30 original questions per language |
| [Source matrix](sources/source-matrix.md) | Started: separates what was checked from what a report claimed |
| [Uncertainty register](docs/uncertainty-register.md) | Started |
| [Labs plan](labs/README.md) | Lab 1 documented; interactive session not run. Labs 2 to 4 and self-assessment executed locally |
| [Module 8 – Capstone architecture review](docs/en/08-capstone-architecture-review.md) | Draft, written |
| [Glossary](docs/en/glossary-terms.md) and [beginner FAQ](docs/en/faq-beginners.md) | 30 terms linked to module sections; 12 beginner questions |

Nothing here claims TM Forum conformance. A lab running locally proves that the lab runs, not that a product is conformant.

## Companion tools

Two small tools grew out of the modules. Both run offline, ship with tests and bilingual messages, and were tried on real public files.

| Tool | Use it with | What it does |
|---|---|---|
| [openapi-sentinel](https://github.com/jihedbfr-art/openapi-sentinel) | [Module 4](docs/en/04-open-apis-in-practice.md) | Checks an OpenAPI/Swagger description against the habits seen in public telecom APIs, and lists the changes between two versions that would break callers |
| [component-manifest-lint](https://github.com/jihedbfr-art/component-manifest-lint) | [Module 5](docs/en/05-components-in-practice.md) | Checks a component manifest against the published schema before it reaches a cluster: unknown fields, missing required fields, wrong types, mismatches with its own services |

They are independent projects, not part of this study path, and say nothing about TM Forum conformance.

## Rules for the content

- Original wording only. No copied specification text, UML schema, figure or exam question.
- Every statement about TM Forum points to a public source with the date it was read.
- Anything unverified is marked "to confirm", never filled in with a guess.
- Every page exists in English and French.
- Synthetic data only. No customer data, no secrets.

## Licences

Code: [Apache License 2.0](LICENSE). Written content: [CC BY 4.0](LICENSE-CONTENT).

## Contributing

Corrections to a source or a version are the most useful contribution. Open an issue with the page, the claim and the public source that contradicts it.

---

<p align="center">
  <img src="assets/jihedailabs-logo.svg" alt="JihedAiLabs" width="80" height="80"><br>
  <sub>Built and maintained under <b>JihedAiLabs</b>.</sub>
</p>
