# Module 0 – Découvrir l'ODA

[English version](../en/00-discovering-oda.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Les sources et leurs limites sont listées dans la [matrice des sources](../../sources/source-matrix.fr.md).

## L'idée en un paragraphe

Un opérateur télécom fait tourner beaucoup d'informatique : commande, facturation, catalogue, activation réseau, traitement des incidents. Pendant des années, chacun de ces éléments était un système séparé et fortement couplé. L'Open Digital Architecture, ou ODA, est la réponse de TM Forum : décrire le métier avec un vocabulaire partagé, découper le logiciel en composants aux interfaces standard, et les exécuter sur une plateforme commune. C'est un plan d'architecture, pas un produit à installer.

## Cinq éléments à ne pas confondre

| Élément | La question à laquelle il répond | L'image en une ligne |
|---|---|---|
| Business Process Framework (eTOM) | Que fait l'opérateur, de bout en bout ? | Une carte des processus métier |
| Information Framework (SID) | De quoi parle le métier ? | Un vocabulaire partagé : client, produit, service, ressource |
| Functional Framework | Quelles fonctions se regroupent ? | Des blocs pour les applications ; sa relation avec l'Application Framework (TAM) reste à confirmer (U5) |
| Open APIs | Comment les systèmes se parlent-ils ? | Des interfaces REST standard pour des fonctions métier |
| Composants ODA et Canvas | Comment est-ce construit et exécuté ? | Des composants déployables, et l'environnement d'exécution qui les héberge |

Les confondre est l'erreur de débutant la plus fréquente. eTOM parle de processus, SID de données, et ni l'un ni l'autre n'est un logiciel.

## Ce qui est vérifiable aujourd'hui

Une partie de ce qui précède peut être consultée directement dans des dépôts publics, ce qui rend le sujet concret.

- L'environnement d'exécution est open source. L'implémentation de référence du Canvas se trouve dans `tmforum-oda/oda-canvas`, sous licence Apache-2.0. Au 15 octobre 2026, ses dernières versions étaient de la série 1.2, avec une préversion (release candidate) 1.2.6 datée du 14 octobre.
- Un composant est décrit par un manifeste. La définition de ce manifeste dans le Canvas porte actuellement quatre versions : `v1beta2`, `v1beta3`, `v1beta4` et `v1`. Aucune version recommandée n'est établie (U2 reste ouverte), et certaines pages de guidelines décrivent encore la `v1beta2`.
- Les API standard sont publiées dans une organisation publique distincte, `tmforum-apis`, qui comptait 97 dépôts à la même date. La licence est indiquée dépôt par dépôt : à vérifier avant de réutiliser un fichier.

## Exercice

Prenez cette histoire synthétique : un client commande un forfait mobile, le forfait est activé, puis la première facture est émise.

1. Listez les étapes métier avec vos propres mots. C'est le côté eTOM.
2. Listez les objets que manipulent ces étapes : client, commande, forfait, ligne. C'est le côté SID.
3. Pour chaque étape, nommez le système qui agirait et l'interface qu'il appellerait. C'est le côté Open API et composants.
4. Décidez lesquels de vos composants tourneraient sur un Canvas, et lesquels resteraient à l'extérieur.

Il n'y a pas de réponse unique. Comparez votre découpage avec celui de quelqu'un d'autre et expliquez les différences.

## Vérifiez-vous

- Savez-vous dire pourquoi eTOM et SID ne sont pas des logiciels ?
- Savez-vous expliquer la différence entre un composant et la plateforme qui l'exécute ?
- Pourquoi un lab qui tourne en local ne prouve-t-il pas la conformité ?

## Limites de ce module

Il explique des concepts et ne reproduit aucun texte officiel. Les modèles complets d'eTOM et de SID ne sont pas publics. Un numéro de version du SID est affiché sur la page de présentation publique, alors que celui d'eTOM reste à confirmer ; l'état actuel est suivi dans le [registre d'incertitudes](../uncertainty-register.fr.md).
