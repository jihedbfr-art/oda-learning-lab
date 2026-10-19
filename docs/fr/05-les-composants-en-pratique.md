# Module 5 – Les composants en pratique

[English version](../en/05-components-in-practice.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : [module 3](03-le-functional-framework-en-pratique.md) et [module 4](04-les-open-apis-en-pratique.md). Tous les noms et contrats de l'exemple sont inventés.

## Donner une frontière aux responsabilités

Le module 3 regroupait le travail en responsabilités. Le module 4 décrivait les contrats qui franchissent une frontière. Il faut maintenant décider quelles responsabilités regrouper et ce que leur implémentation promet aux appelants. Une description utile nomme le travail possédé, le contrat exposé et les contrats consommés. Elle doit rester compréhensible avant de choisir un langage, une base ou une plateforme de déploiement.

Dans notre exercice, le bureau des commandes vérifie une demande de préparation et conserve son lien avec l'accord forfait. Il n'affecte aucune SIM, n'annonce aucune disponibilité réseau et ne calcule aucune facture. Cette frontière donne matière à discussion : le bureau dispose-t-il des informations nécessaires pour accepter le travail, et qui prend ensuite le relais ?

## Ce que le concept public établit

La [présentation officielle](https://www.tmforum.org/oda/implementation-architecture/components-canvas), lue le 2026-10-16, présente les composants comme des unités logicielles réutilisables regroupant des fonctions logiques et exposant leurs fonctionnalités par des Open APIs. Elle décrit aussi des définitions lisibles par machine et une exécution sur un Canvas ODA. Ces éléments établissent le concept publié, pas le statut de notre exercice.

L'[annuaire public](https://www.tmforum.org/oda/directory/), lu le 2026-10-16, indique que les fournisseurs entretiennent leurs propres correspondances fonctionnelles. Une entrée d'annuaire ne prouve donc pas que notre fichier Python réussit une évaluation de certification. Les exigences exactes d'un composant officiel, la version de manifeste recommandée et le rattachement de notre exemple restent **à confirmer**. U2 reste ouverte dans le [registre](../uncertainty-register.fr.md). Aucun inventaire, schéma ou dessin officiel n'est reproduit.

## Exemple traité

Poursuivez l'histoire du forfait mobile. L'étagère des offres présente un achat possible. Le bureau des commandes reçoit une demande liée à `agreement-A` et `offer-B`. Ces références sont des jetons synthétiques, sans identifiant client. Les champs `agreement` et `offer` appartiennent à notre exercice ; aucun attribut standard n'est revendiqué.

| Frontière | Responsabilité ou contrat inventé | Preuve dans le lab |
|---|---|---|
| Travail possédé | Vérifier la demande et conserver la référence de l'accord | Une demande validée produit un résultat préparé |
| Contrat exposé | `prepare` accepte deux chaînes non vides | Champs absents et types incorrects sont rejetés |
| Contrat consommé | L'étagère propose `read-offer` | Le nom de cette dépendance doit être déclaré |
| Sortie | Retourner le même accord avec l'état `prepared` | Le test de réussite compare les deux champs |

Le dictionnaire retourné par `describe()` annonce cette petite conception. `prepare()` contrôle la forme de la demande et les noms de dépendances fournis. Son résultat signifie uniquement que la préparation est faite. Aucun atelier connexion ne travaille derrière ce résultat ; personne ne prétend qu'un abonné peut utiliser la data.

L'opération consommée est déclarée, sans être appelée. Fournir le nom `offer-shelf` ne prouve ni l'existence d'une offre ni la disponibilité d'une autre implémentation. Une dépendance `charge-desk` non déclarée est rejetée avant tout résultat. Une dépendance cachée devient ainsi visible sans ajouter de serveur ni d'appel réseau.

## Comparer deux déclarations

Le [lab 5](../../labs/05-contract-drift/README.fr.md) compare deux déclarations inventées d'opérations et de champs de requête plats. Sa règle de revue classe l'ajout d'un champ optionnel comme compatible, un champ devenu obligatoire ou un type élargi comme à examiner, et le retrait d'une opération, le retrait d'un champ obligatoire ou un changement de type incompatible comme rupture. Rendre un champ obligatoire peut déjà casser un appelant ; le classement à examiner demande de vérifier les usages sans supposer leur sécurité.

Un type s'élargit lorsque l'ensemble accepté grandit strictement : `integer` vers `number`, ou `string` vers `["string", "null"]`, dans cet exercice. Les types inconnus sont rejetés. Ces règles appartiennent à notre format pédagogique et ne constituent pas une politique universelle de compatibilité.

Deux déclarations identiques peuvent masquer un changement de comportement. Leur comparaison n'appelle aucune opération et n'observe ni ordre des événements, persistance ou idempotence ; il faut des preuves d'exécution telles que le rejeu distinct du lab 4.

## Erreurs à éviter

- Faire d'un bloc fonctionnel une frontière de déploiement automatique. Expliquez pourquoi ses responsabilités devraient évoluer ensemble.
- Décrire seulement les contrats exposés. L'appelant doit aussi comprendre les échecs liés aux services consommés.
- Lire `prepared` comme `active`. Chaque état demande un sens précis et des preuves adaptées.
- Présenter une description inventée comme un manifeste officiel. Une lecture facile par machine n'établit aucune conformité.

## Exercice

Exécutez le [lab 3](../../labs/03-component-contract/README.fr.md). Prévoyez le résultat si `agreement` manque, si `offer` devient un nombre et si les dépendances comprennent le bureau des frais. Lancez les tests et comparez les points de rejet à vos prévisions.

Sur papier, ajoutez l'atelier connexion du module 3. Indiquez ce qu'il reçoit, ce qu'il possède et la preuve justifiant un avis de disponibilité. Décidez comment signaler un échec sans perdre la référence de l'accord. Comparez deux frontières possibles avec un collègue. Gardez les choix techniques pour après l'explication des responsabilités et de la reprise sur erreur.

## Vérifiez-vous

- Quelle responsabilité le bureau possède-t-il, expose-t-il et consomme-t-il ?
- Que ne prouve pas une dépendance déclarée sur le comportement à l'exécution ?
- Quelle preuve supplémentaire justifierait d'annoncer une connexion fonctionnelle à l'acheteur ?

## Limites de ce module

Le lab est un exercice original de contrat local, en bibliothèque standard Python. Il ne gère ni persistance, authentification, concurrence, découverte de services ou déploiement. Les tests établissent seulement les règles d'entrée et de dépendances décrites. Ils ne prouvent aucune conformité TM Forum ni interopérabilité réelle. Conservez les sources datées ci-dessus auprès de la [matrice](../../sources/source-matrix.fr.md) pour relire le concept public.
