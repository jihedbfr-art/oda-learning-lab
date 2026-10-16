# Lab 3 – A component contract

[Version française](README.fr.md)

Follow the synthetic mobile-plan story in [Module 5](../../docs/en/05-components-in-practice.md). The order desk announces responsibilities and invented exposed and consumed contracts through `describe()`. These dictionaries are our own design, not an official manifest.

## Run

Python 3 and its standard library are sufficient. From the repository root:

```console
python labs/03-component-contract/component.py
python -m unittest discover -s labs/03-component-contract -p test_component.py
python tools/check_docs.py
```

Executed locally on 2026-10-16: the script printed its declaration and returned `{"agreement": "agreement-A", "state": "prepared"}`. Eight tests passed. Tests cover the declaration, valid result, each missing field, incorrect types and empty values, undeclared dependencies, missing dependencies, invalid containers and extra fields, and mutation isolation.

## Try the boundary

Predict the result before changing a disposable copy of the request:

1. Remove `agreement`: preparation must fail.
2. Set `offer` to the integer `7`: preparation must fail.
3. Add `charge-desk` to the dependency set: preparation must fail.
4. Remove `offer-shelf`: the required dependency is missing.
5. Restore both non-empty string references and the declared dependency. Preparation returns the same agreement.

`prepare(request, dependencies)` accepts exactly the announced fields. Dependencies are a set of declared names; the supplied set must match the consumed dependencies. A fresh dictionary is returned by every `describe()` call, so a reader cannot change future declarations by editing an earlier result.

## Read the result carefully

`prepared` means request validation succeeded. It does not mean network activation. `read-offer` is an announced dependency operation; no catalogue lookup happens. The lab checks names, not remote service availability or offer existence. It performs no network access, persistence, billing or deployment. All references are synthetic. No authentication, concurrency or official conformance is tested. Cost: local execution only, with no paid service. See [NOTICE](../../NOTICE.md).
