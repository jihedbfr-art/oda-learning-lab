# Labs

[English version](README.md)

Le lab 1 est documenté ; les labs 2 et 3 restent prévus. Le guide distingue les tests exécutés de la session interactive non exécutée.

Tous les labs tournent en local, n'utilisent que des données synthétiques, ne demandent aucun service payant et ne revendiquent aucune conformité TM Forum.

| Lab | Objectif | Point de départ | État |
|---|---|---|---|
| 1. La portabilité de numéro comme processus | Suivre un processus multi-opérateurs avec délais et compensation, puis relier chaque étape aux éléments du module 0 | Le dépôt public existant [`bpmn-provisioning-patterns`](https://github.com/jihedbfr-art/bpmn-provisioning-patterns) (Camunda, Spring Boot, Kafka) | [Documenté](01-number-portability/README.fr.md) |
| 2. Un petit catalogue produit | Construire une petite API de catalogue sur données synthétiques et comparer sa forme à une spécification Open API publique | Une spécification publique de `tmforum-apis`, après vérification de sa licence | Prévu |
| 3. Un composant sur un Canvas local | Décrire un composant « hello » avec un manifeste `v1` et l'exécuter sur un cluster Kubernetes local | L'implémentation de référence publique `tmforum-oda/oda-canvas` | Prévu ; lourd, donc planifié plutôt qu'exécuté à chaque push |

Chaque lab indiquera ses prérequis, ses commandes, les assertions à satisfaire, ses limites et son coût d'exécution.
