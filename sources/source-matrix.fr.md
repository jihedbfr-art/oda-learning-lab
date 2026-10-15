# Matrice des sources

[English version](source-matrix.md)

Les dates sont celles du 15 octobre 2026, sauf indication contraire. « Vérifié » signifie lu directement à la source publique à cette date. « Rapporté » signifie que l'information vient d'un rapport de recherche et n'a pas été vérifiée par nous. Une affirmation rapportée ne doit pas être reprise comme un fait ailleurs dans ce dépôt.

## Vérifié

| Sujet | Affirmation | Source | Date | Limite |
|---|---|---|---|---|
| Licence d'ODA Canvas | Apache-2.0 | <https://github.com/tmforum-oda/oda-canvas> | 2026-10-15 | Licence de ce dépôt uniquement |
| Versions d'ODA Canvas | Série 1.2 ; release candidate 1.2.6-rc5 publiée le 2026-10-14 | <https://github.com/tmforum-oda/oda-canvas/releases> | 2026-10-15 | Candidate, pas une version stable |
| Versions du manifeste de composant | La définition du composant dans le chart du Canvas déclare `v1beta2`, `v1beta3`, `v1beta4` et `v1` | `charts/oda-crds/templates/oda-component-crd.yaml` dans `tmforum-oda/oda-canvas` | 2026-10-15 | Dit ce que le Canvas accepte, pas ce que TM Forum recommande |
| Version des guidelines de conception | La page des guidelines de conception des composants ODA décrit la `v1beta2` | <https://tmforum-oda.github.io/oda-ca-docs/docs/ODAComponentDesignGuidelines.html> | 2026-10-15 | La page est en retard sur le Canvas |
| Licence de la documentation | `oda-ca-docs` ne déclare aucune licence | <https://github.com/tmforum-oda/oda-ca-docs> | 2026-10-15 | Rien n'en est copié |
| Taille des organisations GitHub | `tmforum-oda` : 20 dépôts publics ; `tmforum-apis` : 97 | <https://github.com/tmforum-oda>, <https://github.com/tmforum-apis> | 2026-10-15 | Les nombres évoluent |

## Rapporté, non vérifié

| Sujet | Affirmation rapportée | Origine | Pourquoi non vérifié |
|---|---|---|---|
| Catalogue de cours et règles d'examen | Examens en ligne, livres ouverts, 2 tentatives, validité de 3 ans | Rapport de recherche, page `tmforum.org/learn/education/exams/` | L'accès automatisé à tmforum.org est refusé |
| Examens réservés aux membres | Réservés aux membres pour certains bundles « career » | Rapport de recherche | Un second rapport cite une source de 2015 ; non confirmé |
| Conditions d'utilisation du site | La reproduction des contenus du site est limitée | `tmforum.org/legal/website-terms-of-use/` tel que cité | Non lues directement |
| Licence des Open APIs | Apache-2.0 sur les dépôts d'API publics | Rapport de recherche | À vérifier dépôt par dépôt |

## Inutilisable

- Deux pages de parcours de certification citées par un rapport ont renvoyé une erreur 404 à l'ouverture le 2026-10-15 : `tmforum.org/training-certification/oda-components-certification-path/` et `training.tmforum.org/tm-forum-open-api-certification-path`. Les prix rattachés à ces pages dans ce rapport n'ont aucune source et ne sont pas utilisés.
- Les prix des cours ne sont volontairement pas suivis ici. Voir le site officiel.
