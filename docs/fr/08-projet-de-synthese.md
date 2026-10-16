# Module 8 – Projet de synthèse

[English version](../en/08-capstone-architecture-review.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : modules 1–7. Tout est inventé.

## L'opérateur fictif

L'opérateur fictif de cet exercice vend un forfait mobile depuis une étagère des offres. Son bureau des commandes enregistre le choix et crée un accord forfait. Un atelier connexion demande une affectation à la réserve de kits, puis indique si la connexion demandée fonctionne. Un bureau des nouvelles prévient l'acheteur. Les notes d'usage alimentent le bureau des frais, qui prépare la première feuille de frais. Ensuite, la data tombe en panne. Le bureau des pannes ouvre une note et demande à l'atelier d'examiner le kit attribué. Le rétablissement doit rester lié à l’accord avant d'envisager un ajustement. Les messages peuvent arriver deux fois, tard ou avant leurs prédécesseurs. L'opérateur souhaite repérer les relais perdus sans choisir de technologie. Son équipe de revue dispose uniquement de données synthétiques et d'exercices locaux. Elle doit distinguer conception proposée et comportement observé, puis identifier les preuves manquantes avant toute décision de mise en exploitation.

## Dix questions de revue

Les preuves sont attendues, sans présumer leur existence.

| # | Question | Module | Preuve attendue |
|---|---|---|---|
| 1 | Quel flux et quel domaine portent le relais défaillant ? | [1](01-etom-en-pratique.md) | Parcours annoté |
| 2 | Que change un remplacement de SIM ? | [2](02-le-sid-en-pratique.md) | Liens entre objets avant/après |
| 3 | Quelle référence relie achat et réparation ? | [2](02-le-sid-en-pratique.md) | Fiches synthétiques liées |
| 4 | Qui décide de la disponibilité, qui prévient l'acheteur ? | [3](03-le-functional-framework-en-pratique.md) | Tableau des responsabilités |
| 5 | Qu'est-ce qui distingue acceptation et achèvement ? | [4](04-les-open-apis-en-pratique.md) | Exemples distincts d'accusé et de disponibilité |
| 6 | Une fiche d'inventaire commande-t-elle l'activation ? | [4](04-les-open-apis-en-pratique.md) | Frontière et interaction manquante explicites |
| 7 | Que possède et expose le composant de commande ? | [5](05-les-composants-en-pratique.md) | Déclaration et preuve de rejet |
| 8 | Quelle dépendance consommée reste sans test ? | [5](05-les-composants-en-pratique.md) | Liste des dépendances et preuve manquante |
| 9 | Qu'est-ce qui empêche un double ajustement ? | [6](06-assurance-et-facturation-en-pratique.md) | Résultat du rejeu et limite de reprise |
| 10 | Qui traite un prédécesseur absent ou une revue tardive ? | [6](06-assurance-et-facturation-en-pratique.md) | Trace des attentes et responsable |

## Exemple traité

**Proposition discutable, pas un corrigé officiel.** Ces réponses proposent preuves et responsabilités, sans système déployé.

1. La préparation relève du fulfilment, côté client puis service. La panne data traverse client, service et ressource en assurance ; l'ajustement ajoute le billing.
2. Modifiez le kit attribué en conservant accord forfait et promesse de connexion. Comparez les liens avant et après remplacement.
3. Conservez `agreement-A` dans préparation, disponibilité, panne et ajustement. Une référence d'incident distincte sépare les réparations du même achat.
4. L'atelier décide de la disponibilité technique ; le bureau des nouvelles la communique. Le bureau des pannes possède l'investigation, celui des frais la décision d'ajustement.
5. Accepter la demande signifie que la préparation a réussi. Exigez une preuve distincte de rétablissement ou de disponibilité avant d'annoncer une connexion fonctionnelle.
6. L'inventaire décrit une instance enregistrée. Gardez l'activation réseau comme interaction manquante plutôt que d'inventer un endpoint.
7. Le bureau vérifie la demande et conserve l'accord. Son contrat inventé `prepare` rejette champs absents, types incorrects et dépendances non déclarées au lab 3.
8. Déclarez `offer-shelf` et `read-offer`. Le lab 3 vérifie seulement les noms ; existence de l'offre et disponibilité distante restent à prouver.
9. Le lab 4 démontre trois crédits inventés plutôt que six avec déduplication et ordre. Après arrêt, atomicité durable de l'ajustement et mémorisation d'identité restent non prouvées.
10. Sans rétablissement, laissez ajustement et revue en attente. Confiez l'enquête au bureau des pannes avec l'atelier. Signalez une revue tardive et traitez-la après ses prédécesseurs ; le retard seul ne l'invalide pas.

## Erreurs à éviter

- Faire de chaque responsabilité une application séparée.
- Présenter un crédit proposé comme droit acquis ou ajustement réel.
- Prendre un rejeu local pour une preuve de traitement durable.

## Exercice

Remplacez la SIM puis retirez le rétablissement d'une copie jetable. Répondez aux dix questions avec une preuve chacune. Contestez la proposition en regroupant deux responsabilités ; expliquez le compromis sans changer le sens de la disponibilité.

## Vérifiez-vous

Classez chaque réponse : sans aide, après relecture ou floue. Nommez une preuve manquante et son responsable. Organisez la révision avec le [module 7](07-preparer-les-certifications.md), sans nouveau fait sur les certifications ici.

## Limites de ce module

Aucune étude de cas réelle, intégration, mise en production ou évaluation de conformité TM Forum. Les preuves des labs restent locales. Consultez la [matrice](../../sources/source-matrix.fr.md) et le [registre](../uncertainty-register.fr.md) pour les affirmations externes ; aucune question ouverte n'est tranchée.
