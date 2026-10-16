# Module 3 – Le Functional Framework en pratique

[English version](../en/03-functional-framework-in-practice.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : [module 1](01-etom-en-pratique.md) et [module 2](02-le-sid-en-pratique.md).

## Donner une place fonctionnelle au travail

Un processus décrit le travail à réaliser. Un modèle d’information explique les objets concernés. Une vue fonctionnelle demande quelles responsabilités le logiciel doit assurer pour traiter ces objets. TM Forum présente son Functional Framework comme une vue partagée des activités et fonctions liées, côté systèmes ([présentation officielle](https://www.tmforum.org/oda/information-systems/functional-framework/), lue le 2026-10-16).

Pratiquons cette distinction avec notre forfait mobile. Chaque bloc ci-dessous porte un nom courant inventé. Aucun n’est un libellé officiel du framework ni une frontière d’application imposée.

## Trois vues du même relais

| Vue | Question | Notre exemple de commande |
|---|---|---|
| Processus, module 1 | Quel travail, dans quel domaine métier et quel flux ? | Vérifier le changement ; client puis service, fulfilment |
| Information, module 2 | Quels objets gardent leur sens au passage du relais ? | Accord forfait et fiche de préparation |
| Fonction, cet exercice | Quelle responsabilité traite cette information ? | Le bureau des commandes prépare le travail de l’atelier connexion |

Un bloc fonctionnel n’est pas forcément un composant déployable. Les applications peuvent combiner ou partager des responsabilités, avec des règles claires. Une boîte ne tranche pas cette conception.

## Exemple traité

Séquence synthétique : choix du forfait, connexion, première facture, puis panne data. Faites circuler les objets inventés au module 2.

| # | Étape et domaine métier | Objets traités | Bloc fonctionnel inventé |
|---|---|---|---|
| 1 | Choisir et confirmer ; client | Note acheteur, accord forfait | Étagère des offres et bureau des commandes |
| 2 | Vérifier et préparer ; client puis service | Accord forfait, fiche de préparation | Bureau des commandes |
| 3 | Préparer la connexion ; service | Fiche de préparation, promesse de connexion | Atelier connexion |
| 4 | Affecter les moyens ; ressource | Demande de kit, kit attribué | Réserve de kits |
| 5 | Annoncer la disponibilité ; client | Avis de disponibilité, accord forfait | Bureau des nouvelles |
| 6 | Relever et facturer l’usage ; client avec apport ressource | Note d’usage, feuille de calcul des frais | Bureau des frais |
| 7 | Examiner une panne data ; client, service, ressource | Note de panne, promesse de connexion, kit attribué | Bureau des pannes, atelier connexion et réserve de kits |

Les lignes 1 à 5 relèvent du fulfilment, la 6 du billing et la 7 de l’assurance, selon l’exemple pédagogique du module 1. Le même atelier connexion sert à la fourniture et à l’investigation. Chaque flux n’a donc pas besoin de sa propre copie de chaque fonction.

Supposez que la réserve affecte une SIM de remplacement sans changer l’accord forfait. L’atelier connexion doit recevoir la nouvelle affectation avant que le bureau des nouvelles annonce la réussite. Qui décide de la disponibilité, quel lien identifie la connexion, et si l’annonce arrive d’abord ? Ces questions révèlent les responsabilités manquantes.

## La place du TAM

La matrice vérifiée et U5 indiquent que TM Forum présente le Functional Framework comme une évolution de l’Application Framework (TAM), désormais historique, sur la page citée. Cela établit cette relation publique seulement. Une correspondance complète de migration ou le retrait de tous les documents TAM restent à confirmer ; rien de tel n’est déduit ici.

## Erreurs à éviter

- **Transformer chaque étape en application.** Plusieurs étapes peuvent employer une même fonction.
- **Confondre domaine métier et bloc.** « Ressource » désigne une vue du travail ; notre réserve de kits désigne une responsabilité de l’exemple.
- **Dupliquer les fonctions par flux.** Vérifiez d’abord si l’information et la décision diffèrent réellement.
- **Choisir la technologie trop tôt.** Expliquez qui possède la décision avant de choisir un produit ou un déploiement.

## Exercice

Reprenez votre relais et votre liste d’objets des modules 1 et 2. Regroupez le travail en blocs nommés sans glossaire. Pour chacun, indiquez entrée, sortie et responsable de la décision. Gardez le domaine métier et le flux à côté.

Ajoutez le remplacement de SIM. Réutilisez un bloc si sa responsabilité reste identique. Placez une panne à une frontière et expliquez qui la détecte, qui récupère et quel objet relie cette reprise à l’achat. Comparez deux découpages et défendez votre choix. Aucun corrigé officiel n’est fourni.

## Vérifiez-vous

- Pourquoi une fonction peut-elle servir au fulfilment et à l’assurance ?
- Que manque-t-il à un bloc avec entrée et sortie, sans responsable de décision ?
- Pourquoi une vue fonctionnelle ne détermine-t-elle pas un composant déployable ?

## Limites de ce module

Exercice original, sans carte officielle, version revendiquée ni conformité. Consultez la [matrice](../../sources/source-matrix.fr.md) et le [registre d’incertitudes](../uncertainty-register.fr.md), notamment U5. Les frontières de composants et contrats d’interface demandent une conception distincte ; ce tableau ne les décide pas.
