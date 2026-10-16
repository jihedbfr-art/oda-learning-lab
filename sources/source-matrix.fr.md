# Matrice des sources

[English version](source-matrix.md)

Les lignes historiques du 15 octobre 2026 sont conservées sans nouvelle validation. Les ajouts datent du 16 octobre 2026. « Vérifié » signifie lu directement à la source publique ; un résultat de recherche seul ne suffit pas. Les affirmations non vérifiées ne doivent pas devenir des faits ailleurs dans ce dépôt.

## Vérifié

| Sujet | Affirmation | Source | Date | Limite |
|---|---|---|---|---|
| Licence d'ODA Canvas | Apache-2.0 | <https://github.com/tmforum-oda/oda-canvas> | 2026-10-15 | Licence de ce dépôt uniquement |
| Versions d'ODA Canvas | Série 1.2 ; release candidate 1.2.6-rc5 publiée le 2026-10-14 | <https://github.com/tmforum-oda/oda-canvas/releases> | 2026-10-15 | Candidate, pas une version stable |
| Versions du manifeste de composant | La définition du composant dans le chart du Canvas déclare `v1beta2`, `v1beta3`, `v1beta4` et `v1` | `charts/oda-crds/templates/oda-component-crd.yaml` dans `tmforum-oda/oda-canvas` | 2026-10-15 | Dit ce que le Canvas accepte, pas ce que TM Forum recommande |
| Version des guidelines de conception | La page des guidelines de conception des composants ODA décrit la `v1beta2` | <https://tmforum-oda.github.io/oda-ca-docs/docs/ODAComponentDesignGuidelines.html> | 2026-10-15 | La page est en retard sur le Canvas |
| Licence de la documentation | `oda-ca-docs` ne déclare aucune licence | <https://github.com/tmforum-oda/oda-ca-docs> | 2026-10-15 | Rien n'en est copié |
| Taille des organisations GitHub | `tmforum-oda` : 20 dépôts publics ; `tmforum-apis` : 97 | <https://github.com/tmforum-oda>, <https://github.com/tmforum-apis> | 2026-10-15 | Les nombres évoluent |
| Format des examens | En ligne, QCM, à livre ouvert, sans surveillance ni aide humaine ; Awareness/Fundamentals : 40 questions en 1 h ; Practitioners : 40 ou 60 en 1 ou 2 h | <https://www.tmforum.org/learn/education/exams/> | 2026-10-16 | Selon le niveau et le sujet |
| Tentatives et validité | Deux tentatives par défaut ; nouvelle tentative sur demande après 14 jours ; certification valable trois ans | <https://www.tmforum.org/learn/education/exams/> | 2026-10-16 | Validité du certificat distincte de l'accès au package |
| Prérequis d'examen | Practitioners exige le Fundamentals correspondant ; examen à tenter avant expiration de l'accès au lot de formation | <https://www.tmforum.org/learn/education/exams/> | 2026-10-16 | Aucune durée universelle d'accès déduite |
| Accès membre | La page publique réserve les examens de certification aux personnes travaillant pour une entreprise membre | <https://www.tmforum.org/learn/certification/assessments/prove-your-mettle/> | 2026-10-16 | Déclaration générale ; pas de liste actuelle des exceptions ou bundles |
| Conditions du site | Usage personnel permis ; usage commercial des contenus ODA soumis aux notices/licences ; reproduction et redistribution exigent une permission sauf exception explicite | <https://www.tmforum.org/legal/website-terms-of-use/> | 2026-10-16 | Last Modified affiché : 16 June 2025 ; copies personnelles limitées permises, pas de republication générale ; résumé, pas avis juridique |
| SID : métadonnées publiées | La page officielle liste GB922 Information Framework Models Suite et Standards Addenda v26.0, approbation d'équipe du 12 octobre 2026 | <https://www.tmforum.org/open-digital-architecture/information-framework-sid/> | 2026-10-16 | Métadonnées visibles ; modèles complets non consultés ; pas de garantie qu'aucune version plus récente existe |
| Accessibilité publique | Pages examens, éducation et présentation SID lues sans compte | <https://www.tmforum.org/learn/education/> | 2026-10-16 | Page d'éducation seulement ; aucune connexion ni inscription ou épreuve essayée ; voir U6 |
| TMF620_ProductCatalog | Apache-2.0, fichier LICENSE lu | <https://github.com/tmforum-apis/TMF620_ProductCatalog/blob/main/LICENSE> | 2026-10-16 | Ce dépôt uniquement ; conserver les notices ; aucun fichier copié |
| TMF622_ProductOrder | Apache-2.0, fichier LICENSE lu | <https://github.com/tmforum-apis/TMF622_ProductOrder/blob/main/LICENSE> | 2026-10-16 | Ce dépôt uniquement ; conserver les notices ; aucun fichier copié |
| TMF638_ServiceInventory | Apache-2.0, fichier LICENSE lu | <https://github.com/tmforum-apis/TMF638_ServiceInventory/blob/main/LICENSE> | 2026-10-16 | Ce dépôt uniquement ; conserver les notices ; aucun fichier copié |
| TMF637_ProductInventory | Apache-2.0, fichier LICENSE lu | <https://github.com/tmforum-apis/TMF637_ProductInventory/blob/main/LICENSE> | 2026-10-16 | Ce dépôt uniquement ; conserver les notices ; aucun fichier copié |
| TMF639_ResourceInventory | Apache-2.0, fichier LICENSE lu | <https://github.com/tmforum-apis/TMF639_ResourceInventory/blob/main/LICENSE> | 2026-10-16 | Ce dépôt uniquement ; conserver les notices ; aucun fichier copié |

## Rapporté, non vérifié

| Sujet | Affirmation rapportée | Source | Limite et résultat au 2026-10-16 |
|---|---|---|---|
| Version actuelle eTOM | v26.0 signalée par l’index de recherche officiel ; non confirmée par lecture directe | <https://www.tmforum.org/resources/suite/gb921-business-process-framework-etom-suite-v26-0/> | 403 : inaccessible le 2026-10-16 ; index de recherche insuffisant pour classer « Vérifié » |
| Licences des autres Open APIs | Apache-2.0 aurait une portée générale | <https://github.com/tmforum-apis> | Seulement cinq dépôts vérifiés ; ne pas généraliser |
| Détails des suites SID | Contenu exact des suites v26.0 | <https://www.tmforum.org/resources/model/gb922-information-framework-models-suite-v26-0/> | 403 : inaccessible le 2026-10-16 ; également /resources/suite/gb922-standards-addenda-for-information-framework-suite-v26-0/ |
| Version de manifeste recommandée | Le support de plusieurs versions ne prouve pas une recommandation | <https://github.com/tmforum-oda/oda-canvas> | U2 reste ouvert ; preuve du 15 octobre conservée, pas de nouvelle vérification de recommandation |
| TAM et Functional Framework | Une lecture a rapporté le Functional Framework comme une évolution de l'Application Framework (TAM) ; un recoupement a trouvé des pages de la suite TAM encore présentées comme courantes et aucune mention publique d'un statut réduit | <https://www.tmforum.org/oda/information-systems/functional-framework/> | Non tranché au 2026-10-16 : la page de présentation n'a pas été relue directement lors du recoupement ; n'affirmer aucun statut du TAM (U5) |

Les anciennes lignes examens, accès membre et conditions sont déplacées vers « Vérifié » ; la généralisation des licences reste non vérifiée.

## Inutilisable

- Deux pages de parcours de certification citées par un rapport ont renvoyé une erreur 404 à l'ouverture le 2026-10-15 : `tmforum.org/training-certification/oda-components-certification-path/` et `training.tmforum.org/tm-forum-open-api-certification-path`. Les prix rattachés à ces pages dans ce rapport n'ont aucune source et ne sont pas utilisés.
- Les prix des cours ne sont volontairement pas suivis ici. Voir le site officiel.
