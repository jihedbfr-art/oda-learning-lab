# Module 1 – eTOM en pratique

[English version](../en/01-etom-in-practice.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : [module 0](00-decouvrir-l-oda.md). Les sources et leurs limites sont dans la [matrice des sources](../../sources/source-matrix.fr.md).

## Ce qu'est eTOM, et ce qu'il n'est pas

eTOM est le Business Process Framework de TM Forum. C'est une carte partagée de ce que fait une entreprise télécom, pour que des personnes de sociétés différentes puissent désigner la même chose et l'entendre de la même façon. C'est une manière de classer et de discuter des processus.

Ce n'est pas un workflow, il n'impose aucun ordre d'exécution, et ce n'est pas un logiciel. Une plateforme de facturation peut supporter certains processus eTOM. Elle n'est pas eTOM.

## Lire la carte

On enseigne habituellement la carte selon deux directions, et c'est ce qui la rend utile.

- **Les regroupements horizontaux** séparent le métier selon l'objet du travail. En allant du côté client vers le côté infrastructure, on trouve le travail centré sur le client, sur le service que le client achète, sur les ressources qui le fournissent, et sur les fournisseurs et partenaires concernés.
- **Les flux de bout en bout** traversent ces regroupements. On en enseigne toujours trois : mettre un produit à disposition d'un client (fulfilment), le maintenir en état de marche (assurance) et le facturer (billing).

Un même événement métier a donc deux coordonnées : quelle partie du métier agit, et à quel flux il appartient.

> Ceci est la vue de premier niveau la plus couramment enseignée. Les noms exacts, la numérotation et le nombre de niveaux dépendent de la version publiée du framework, et cette version n'est pas publique en entier. Ne citez aucun numéro de niveau à partir de cette page. Voir U1 dans le [registre d'incertitudes](../uncertainty-register.fr.md).

## Pourquoi les couches comptent

La plupart des vrais problèmes surviennent à un passage de relais. Le client demande un forfait mobile. Quelqu'un doit le transformer en un service à configurer, et quelqu'un d'autre en ressources à allouer. Chaque passage change le vocabulaire : commande client, puis commande de service, puis commande de ressource. Nommer la couche dit qui possède l'étape suivante et où une panne risque de se cacher.

## Exemple traité

L'histoire synthétique du module 0 : un client commande un forfait mobile, le forfait est activé, puis la première facture est émise.

| # | Ce qui se passe | Domaine métier qui agit | Flux |
|---|---|---|---|
| 1 | Le client choisit un forfait et confirme | Client | Fulfilment |
| 2 | La commande est vérifiée et découpée en éléments à mettre en place | Client, puis service | Fulfilment |
| 3 | Le service est configuré pour ce client | Service | Fulfilment |
| 4 | Un numéro et une SIM sont alloués, et le réseau reçoit l'ordre d'activer la ligne | Ressource | Fulfilment |
| 5 | Le client est informé que la ligne est active | Client | Fulfilment |
| 6 | La première consommation est enregistrée et valorisée, puis une facture est émise | Client, avec la consommation venue du côté ressource | Billing |
| 7 | Le client se plaint que la data mobile ne fonctionne pas | Client, puis service, puis ressource | Assurance |

Remarquez que les étapes 2 et 6 touchent deux domaines, et que l'étape 7 descend les couches puis remonte. C'est normal : les événements réels tiennent rarement dans une seule case.

## Erreurs à éviter

- **Le lire comme une séquence.** Les flux décrivent des familles de travail, pas un chemin figé.
- **Aller toujours au niveau le plus fin.** Commencez grossier. Affinez seulement là où une décision en dépend.
- **Confondre un processus et un système.** « Le système de facturation » n'est pas un processus. Ce que le métier en fait, si.
- **Forcer une case par étape.** Si une étape couvre honnêtement deux domaines, notez les deux et dites pourquoi.

## Exercice

Utilisez ces huit événements synthétiques. Pour chacun, indiquez le domaine qui agit et le flux, avec une phrase de justification dans vos propres mots.

1. Un client demande à faire passer sa ligne sur un autre forfait.
2. Une équipe terrain remplace une armoire défectueuse.
3. L'opérateur achète un lot de cartes SIM à un fournisseur.
4. Un client conteste un montant sur sa facture.
5. Une fenêtre de maintenance planifiée est annoncée aux clients concernés.
6. Un schéma de fraude est détecté sur un groupe de lignes.
7. Une nouvelle offre est créée et préparée pour la vente.
8. Un client demande à résilier son abonnement.

Ensuite :

- Trouvez un événement pour lequel deux réponses sont défendables. Expliquez les deux et dites quel passage de relais tranche.
- Choisissez un passage de relais et notez quelles entités le traversent. Vous réutiliserez cette liste dans le module 2 sur le modèle d'information.

Il n'y a volontairement pas de corrigé officiel ici. Le but est de s'exercer au raisonnement, pas de reproduire une cartographie de référence.

## Vérifiez-vous

- Pourquoi un événement a-t-il deux coordonnées ?
- Quel flux est concerné quand un client conteste une facture, et lequel quand un service tombe en panne ?
- Pourquoi nommer un passage de relais est-il plus utile que nommer un seul processus ?

## Limites de ce module

Il enseigne comment lire et utiliser le framework. Il ne copie aucun schéma ni aucune liste de libellés officiels et n'indique aucune version du framework. Le premier niveau de détail que vous ajoutez à votre propre cartographie doit être vérifié sur la page officielle du framework avant publication.
