# Source matrix

[Version française](source-matrix.fr.md)

Dates are 15 October 2026 unless stated. "Checked" means read directly from the public source on that date. "Reported" means it comes from a research report and has not been checked by us. Reported claims must not be repeated as facts elsewhere in this repository.

## Checked

| Subject | Statement | Source | Date | Limit |
|---|---|---|---|---|
| ODA Canvas licence | Apache-2.0 | <https://github.com/tmforum-oda/oda-canvas> | 2026-10-15 | Licence of that repository only |
| ODA Canvas releases | 1.2 line; release candidate 1.2.6-rc5 published 2026-10-14 | <https://github.com/tmforum-oda/oda-canvas/releases> | 2026-10-15 | Candidate, not a stable release |
| Component manifest versions | The component definition in the Canvas chart declares `v1beta2`, `v1beta3`, `v1beta4` and `v1` | `charts/oda-crds/templates/oda-component-crd.yaml` in `tmforum-oda/oda-canvas` | 2026-10-15 | Says what the Canvas accepts, not which one TM Forum recommends |
| Design guidelines version | The ODA component design guidelines page describes `v1beta2` | <https://tmforum-oda.github.io/oda-ca-docs/docs/ODAComponentDesignGuidelines.html> | 2026-10-15 | The page lags the Canvas |
| Documentation licence | `oda-ca-docs` declares no licence | <https://github.com/tmforum-oda/oda-ca-docs> | 2026-10-15 | Nothing is copied from it |
| GitHub organisation size | `tmforum-oda`: 20 public repositories; `tmforum-apis`: 97 | <https://github.com/tmforum-oda>, <https://github.com/tmforum-apis> | 2026-10-15 | Counts change |

## Reported, not checked

| Subject | Reported claim | Where it came from | Why not checked |
|---|---|---|---|
| Course catalogue and exam rules | Exams are online, open book, with 2 attempts and a 3-year validity | Research report, page `tmforum.org/learn/education/exams/` | Automated access to tmforum.org is refused |
| Member-only exams | Reserved for members for some "career" bundles | Research report | A second report cites a 2015 source; not confirmed |
| Website terms | Reproduction of site material is restricted | `tmforum.org/legal/website-terms-of-use/` as cited | Not read directly |
| Open API licence | Apache-2.0 on the public API repositories | Research report | Check each repository |

## Not usable

- Two certification-path pages cited by one report returned a 404 error when opened on 2026-10-15: `tmforum.org/training-certification/oda-components-certification-path/` and `training.tmforum.org/tm-forum-open-api-certification-path`. Prices attached to them in that report have no source and are not used.
- Course prices are deliberately not tracked here. See the official site.
