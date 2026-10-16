# Module 4 – Les Open APIs en pratique

[English version](../en/04-open-apis-in-practice.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : [module 2](02-le-sid-en-pratique.md) et [module 3](03-le-functional-framework-en-pratique.md).

## Un contrat au passage de relais

Le bureau des commandes et l’atelier connexion du module 3 doivent échanger de l’information. Un contrat d’interface définit ce qu’un appelant peut demander et comment le destinataire représente sa réponse. Ce n’est pas le composant qui réalise ce comportement. Deux implémentations peuvent exposer le même contrat avec des choix de stockage et de déploiement différents.

TM Forum publie un programme Open API et des définitions publiques ([présentation officielle](https://www.tmforum.org/oda/open-apis/), lue le 16 octobre 2026). Utilisons cinq dépôts pour choisir une interface adaptée à une interaction métier. Cette correspondance originale n’impose aucune séquence d’implémentation.

## Cinq références, cinq rôles distincts

Numéros, titres et licences ci-dessous ont été vérifiés directement le 16 octobre 2026. Les titres viennent des métadonnées des définitions liées. Définitions et LICENSE pointent vers des commits précis pour rendre la preuve reproductible ; aucun schéma ni exemple de charge utile n’est recopié ici.

| API | Titre de la définition liée | Interaction proposée | Licence du dépôt |
|---|---|---|---|
| TMF620 | [Product Catalog Management](https://github.com/tmforum-apis/TMF620_ProductCatalog/blob/24e69f3026f2b514baa27d7206540fc7b55bcb45/TMF620-ProductCatalog-v4.1.0.swagger.json) | Consulter ce qui peut être proposé avant le choix du forfait | [Apache-2.0](https://github.com/tmforum-apis/TMF620_ProductCatalog/blob/24e69f3026f2b514baa27d7206540fc7b55bcb45/LICENSE) |
| TMF622 | [Product Ordering](https://github.com/tmforum-apis/TMF622_ProductOrder/blob/a3825f95248eb04fb1c7e2321305bc99631168a4/TMF622-ProductOrder-v4.0.0.swagger.json) | Soumettre et suivre la demande d’achat | [Apache-2.0](https://github.com/tmforum-apis/TMF622_ProductOrder/blob/a3825f95248eb04fb1c7e2321305bc99631168a4/LICENSE) |
| TMF638 | [Service Inventory Management](https://github.com/tmforum-apis/TMF638_ServiceInventory/blob/50fc82942e423c81896362d1ab9847f7c918cf7f/TMF638-ServiceInventory-v4.0.0.swagger.json) | Examiner les instances de service associées à la fourniture | [Apache-2.0](https://github.com/tmforum-apis/TMF638_ServiceInventory/blob/50fc82942e423c81896362d1ab9847f7c918cf7f/LICENSE) |
| TMF637 | [Product Inventory](https://github.com/tmforum-apis/TMF637_ProductInventory/blob/f598b4a02186071f2794b8f9b4f6904ef0a8aa52/TMF637-ProductInventory-v4.0.0.swagger.json) | Examiner les instances de produit détenues par le client | [Apache-2.0](https://github.com/tmforum-apis/TMF637_ProductInventory/blob/f598b4a02186071f2794b8f9b4f6904ef0a8aa52/LICENSE) |
| TMF639 | [Resource Inventory Management](https://github.com/tmforum-apis/TMF639_ResourceInventory/blob/2693a854940de3c6e15b1aade24f981d94b75d3a/TMF639-ResourceInventory-v4.0.0.swagger.json) | Examiner les ressources qui portent la connexion | [Apache-2.0](https://github.com/tmforum-apis/TMF639_ResourceInventory/blob/2693a854940de3c6e15b1aade24f981d94b75d3a/LICENSE) |

Versions des définitions choisies : 4.1.0 pour TMF620, 4.0.0 pour les quatre autres. Ce sont des références de lecture, sans affirmation sur la dernière version ni recommandation de déploiement. Apache-2.0 a été vérifiée séparément pour chaque dépôt ; elle n’établit pas la licence d’un autre dépôt ni du site entier. Voir U4 dans le [registre d’incertitudes](../uncertainty-register.fr.md).

## Exemple traité

Reprenez la commande synthétique de forfait mobile. L’étagère des offres consulte d’abord la référence catalogue TMF620 pour expliquer ce qui peut être acheté. L’accord forfait du module 2 conserve le choix ; ce n’est pas une copie de la fiche catalogue.

Le bureau des commandes pourrait ensuite employer TMF622 pour transmettre la demande d’achat. Conservez la référence qui relie demande et accord. Un accusé de réception ne prouve pas que le réseau est prêt. Décidez quelle preuve ultérieure permet au bureau des nouvelles de prévenir l’acheteur.

Après fourniture, une vue d’inventaire aide à distinguer trois questions. TMF637 concerne l’instance de produit détenue par le client, TMF638 l’instance de service et TMF639 les ressources qui la portent. Dans notre vocabulaire inventé, ces vues se rapportent à l’accord, à la promesse de connexion et au kit attribué. Cette comparaison pédagogique n’est pas une correspondance SID ou API champ par champ.

Si le client remplace une SIM, demandez quelle ressource a changé et si l’achat reste identique. Une fiche d’inventaire n’est pas une commande d’activation d’équipement réseau. Ces cinq références ne couvrent pas toutes les interactions techniques nécessaires à l’histoire ; ce module n’invente aucun endpoint d’activation manquant.

## Erreurs à éviter

- **Appeler le composant « l’API ».** Le contrat décrit ce qui franchit une frontière ; une implémentation doit réaliser le travail.
- **Confondre offre et produit détenu.** Le catalogue décrit les possibilités, l’inventaire les instances enregistrées.
- **Prendre une commande acceptée pour une fourniture achevée.** Identifiez la preuve de disponibilité attendue.
- **Combiner des définitions sans vérifier leurs versions.** Des noms proches ne prouvent aucune compatibilité de champs, opérations ou comportement.

## Exercice

Reprenez votre relais et vos objets du module 2. Écrivez une demande d’achat synthétique avec vos propres champs inventés. Indiquez émetteur, destinataire et référence permettant de rattacher une réponse ultérieure. N’utilisez ni identifiant client ni numéro de téléphone réel.

Ouvrez ensuite la définition TMF622 liée. Comparez en privé votre proposition à cette version : quels sens correspondent, quelles informations nécessaires manquent, quelles hypothèses restent les vôtres ? Notez les différences avec vos mots, sans copier de schéma ni d’exemple. Recommencez pour une consultation catalogue, en distinguant l’offre du produit finalement détenu. Votre demande inventée n’est pas une charge utile conforme.

## Vérifiez-vous

- Pourquoi un contrat d’API ne détermine-t-il pas la base interne de l’application ?
- Qu’est-ce qui distingue catalogue, inventaire produit et inventaire de service ?
- Pourquoi cinq définitions et licences accessibles ne prouvent-elles pas une intégration fonctionnelle ?

## Limites de ce module

Aucun serveur, appel, réponse ou test de conformité exécuté. Authentification, interopérabilité des versions et déploiement opérateur non évalués. Lisez la [matrice datée](../../sources/source-matrix.fr.md) avec les références figées. Choisir un contrat est une étape de conception ; implémentation et validation restent des travaux distincts.
