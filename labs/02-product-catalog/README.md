# Lab 2 – A small product catalogue

[Version française](README.fr.md)

This original exercise continues the mobile-plan story from [Module 2](../../docs/en/02-sid-in-practice.md). Work alone, offline, with four invented offers. No customer, subscription or network resource exists in the data.

## The idea

An offer describes what can be chosen. A specification describes reusable capabilities behind that choice. A price describes the exercise charge. Two offers can reuse the same capabilities while charging different amounts. This is our own teaching model, not an official schema.

Read [catalog.json](catalog.json). Its opening `notice` states in both languages that every record is synthetic. `credits` is an invented unit, not a currency or a commercial tariff. `month` is the common comparison period. No tax, usage charge or discount calculation is implied.

| Object | Own fields | Meaning in this exercise |
|---|---|---|
| Specification | `id`, `services` | A reusable list of capabilities |
| Offer | `id`, bilingual `name`, `specification` | A choice linked to one specification |
| Price, inside an offer | `credits`, `period` | A non-negative whole number of credits per month |

`voice` means calls and `mobile-data` means mobile connectivity in this story. They are invented labels. A reusable specification is not an activated service for a particular buyer.

## Run it

Prerequisite: Python 3. No package installation, account, server or network access is needed. From the repository root:

```console
python labs/02-product-catalog/catalog.py
python -m unittest discover -s labs/02-product-catalog -p test_catalog.py
python tools/check_docs.py
```

The script always reads the JSON beside itself, regardless of the working directory. It displays the links and does not write files. Recorded output on 16 October 2026 with Python 3.12.0:

```text
Synthetic data / Données synthétiques
Valid offers / Offres valides: 4
offer-A | spec-talk | voice | 8 credits/month (crédits/mois)
offer-B | spec-data | mobile-data | 12 credits/month (crédits/mois)
offer-C | spec-mix | voice, mobile-data | 18 credits/month (crédits/mois)
offer-D | spec-mix | voice, mobile-data | 15 credits/month (crédits/mois)
```

Five unit tests passed. They check the supplied catalogue, a missing specification reference, duplicate offer identifiers, invalid amounts and invalid collection structures. These tests protect the links and amounts used by the exercise. Validation enforces these exercise constraints, not a complete JSON schema; the learner reads the bilingual notice and names. Malformed or unreadable input produces a bilingual error and exit status 1.

## Guided exercise

1. Draw your own boxes for an offer, a specification and a price. Label their relationships. Which objects are reused?
2. Predict which offers contain mobile data before running the script. Follow each reference instead of guessing from names.
3. Compare C and D. Explain why different prices need not imply different specifications. No eligibility or promotion rule is encoded.
4. In a disposable copy, add a fifth offer with bilingual names, reuse `spec-data` and choose a whole number of invented credits. Run and explain the extra row. Restore the supplied data before running its tests, which expect four offers.
5. In that copy, try an unknown specification reference, then a negative amount. Run after each change, record the rejection and restore the file.
6. Return to the ordering hand-off in Module 2. Which selected offer reference would you carry into the invented plan agreement? What information would still be missing to activate a service?

## One possible reading

B, C and D contain mobile data; A does not. C and D share `spec-mix` and its two capabilities. Their difference is 3 invented credits per month. This comparison is not a bill: no customer has purchased either offer.

## Check yourself and limits

Can you distinguish a reusable specification from an active service? What problem would an unknown reference cause at a hand-off? Why do equal services not establish equal commercial terms?

The executed script demonstrates local reading, link validation and display of synthetic data. It implements no real API and demonstrates no TMF620 conformance. No specification or payload is copied. There is no order handling, persistence, activation, billing engine, security model or performance evidence. Execution uses only your machine and calls no paid service. See the project [notice](../../NOTICE.md).
