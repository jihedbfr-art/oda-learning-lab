# Module 2 – Le SID en pratique

[English version](../en/02-sid-in-practice.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : [module 1](01-etom-en-pratique.md). Gardez son exercice sur les passages de relais à portée de main.

## Un sens partagé avant le choix du stockage

SID est l’Information Framework de TM Forum. Sa présentation publique décrit des définitions métier partagées, indépendantes d’une plateforme, d’un langage ou d’un protocole ([page officielle](https://www.tmforum.org/open-digital-architecture/information-framework-sid/), lue le 16 octobre 2026). Ce module part de cette vocation pour poser une question pratique : quand le travail change de mains, les deux équipes parlent-elles de la même chose ?

Un modèle d’information décrit le sens des objets métier et leurs relations. Un modèle de données fixe des choix d’implémentation : tables ou documents, clés, types et contraintes. Dire qu’un achat peut demander plusieurs étapes techniques de mise en service ne décide pas du nombre de tables à créer. SID n’est ni une base de données ni un logiciel à installer.

## Produit, service et ressource

Pour cet exercice, distinguez ce qui a été acheté, la capacité fournie et les moyens de la fournir. Ces distinctions pédagogiques ne sont pas des définitions de classes officielles du SID.

| Vue | Question dans notre histoire de forfait mobile | Objet inventé pour l’exercice |
|---|---|---|
| Client | Qui demande et où envoyer les nouvelles ? | Note acheteur |
| Produit | Qu’a accepté de recevoir cette personne ? | Accord forfait |
| Service | Quelle capacité doit fonctionner pour elle ? | Promesse de connexion |
| Ressource | Quels moyens techniques portent cette capacité ? | Kit attribué |

Remplacer une SIM change le kit attribué. Cela ne crée pas forcément un nouvel accord forfait. Cette distinction permet au support d’expliquer pourquoi un changement technique ne constitue pas nécessairement un nouvel achat.

## Exemple traité

Reprenez la commande synthétique des modules 0 et 1 : forfait mobile, activation, première facture, puis problème de données mobiles. Tous les noms d’objets ci-dessous sont inventés pour l’exercice. Ce tableau n’est ni un extrait du SID ni une proposition de message standard.

| # | Passage de relais | Objets qui le traversent | Sens à conserver |
|---|---|---|---|
| 1 | Vente vers traitement de commande | Note acheteur, accord forfait | Le choix et l’acheteur restent liés |
| 2 | Commande vers mise en place du service | Fiche de préparation liée à l’accord forfait | La capacité demandée découle de l’achat |
| 3 | Service vers allocation technique | Promesse de connexion, demande de kit | L’allocation sert cette connexion |
| 4 | Allocation vers service | Kit attribué lié à la promesse de connexion | Les moyens sont affectés à la bonne connexion |
| 5 | Service vers contact client | Avis de disponibilité lié à l’accord forfait | La réussite technique devient une nouvelle compréhensible |
| 6 | Collecte des usages vers facturation | Note d’usage, feuille de calcul des frais | La consommation revient au bon accord |
| 7 | Support vers investigation technique | Note de panne, promesse de connexion, kit attribué | L’investigation suit la connexion touchée |

Donnez à l’accord forfait la référence inventée `agreement-A`, puis réutilisez-la dans la fiche de préparation et l’avis de disponibilité. Cette référence d’exercice évite de confondre deux achats ; ce n’est pas un attribut officiel.

## Erreurs à éviter

- **Dessiner les tables trop tôt.** Expliquez d’abord chaque objet à une personne qui ne maintient pas la base.
- **Employer un mot pour plusieurs choses.** « Ligne » peut désigner un achat, une connexion ou un numéro. Demandez ce qui a changé.
- **Transmettre toute la fiche partout.** L’équipe destinataire a besoin du sens et des liens utiles à son travail, pas de tous les détails détenus en amont.
- **Confondre un événement et l’objet.** L’avis de disponibilité signale un changement ; l’accord existe encore après sa réception.

## Exercice

Reprenez les entités listées à la fin du module 1. Nommez-les avec des mots courants et expliquez chacune en une phrase. Dessinez vous-même un petit modèle : des boîtes pour les objets, des liens nommés pour leurs relations.

Choisissez un relais. Indiquez qui crée chaque objet, qui le modifie et quelle référence relie le travail entrant au travail sortant. Remplacez ensuite une SIM sans changer l’achat. Expliquez quelle boîte change et quels liens doivent survivre. Ajoutez enfin une deuxième commande et montrez comment éviter la confusion. Aucun modèle UML officiel n’est nécessaire.

## Vérifiez-vous

- En quoi produit, service et ressource diffèrent-ils dans le remplacement de SIM ?
- Quels choix relèvent du modèle d’information, lesquels du modèle de données implémenté ?
- Quelle preuve montrerait que deux équipes donnent le même sens à une référence partagée ?

## Limites de ce module

Le modèle SID complet et les définitions exactes ne sont pas reproduits ici. La présentation publique liste v26.0 ; les pages détaillées étaient inaccessibles pendant cette vérification. Voir U1 dans le [registre d’incertitudes](../uncertainty-register.fr.md) et la [matrice datée](../../sources/source-matrix.fr.md). Cet exercice ne fournit ni noms, attributs ou schéma officiels, ni preuve de conformité.
