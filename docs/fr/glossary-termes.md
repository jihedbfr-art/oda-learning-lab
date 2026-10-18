# Glossaire du parcours

[English version](../en/glossary-terms.md) · [FAQ pour débuter](faq-debutants.md)

Ces 30 explications reprennent les exemples de nos modules, sans définition ni libellé officiel. La section liée permet de retrouver le raisonnement derrière chaque terme.

La [matrice des sources](../../sources/source-matrix.fr.md) consigne les preuves externes datées ; le [registre d’incertitudes](../uncertainty-register.fr.md) en précise les limites. U1 et U5 restent partielles : ce glossaire n’affirme ni version actuelle du SID ni statut du TAM.

## 1. Processus

Travail que le métier doit réaliser, comme vérifier une commande. Le nommer permet d’en discuter sans choisir le logiciel qui le réalisera.

[Module 1 : Ce qu'est eTOM, et ce qu'il n'est pas](01-etom-en-pratique.md#ce-quest-etom-et-ce-quil-nest-pas)

## 2. Domaine métier

Partie du métier concernée par une étape de notre histoire. Une demande peut traverser le travail côté client, service et ressource ; une étape peut donc concerner plusieurs domaines.

[Module 1 : Lire la carte](01-etom-en-pratique.md#lire-la-carte)

## 3. Flux

Manière de suivre des travaux liés à travers les domaines métier, par exemple la fourniture ou la réparation. Dans ces modules, il regroupe le travail par finalité sans imposer un ordre d’exécution figé.

[Module 1 : Lire la carte](01-etom-en-pratique.md#lire-la-carte)

## 4. Fulfilment

Volet fourniture de notre histoire de forfait mobile, du choix de l’acheteur à une connexion fonctionnelle. Vérifier la commande et attribuer une SIM y contribuent depuis des domaines métier différents.

[Module 1 : Exemple traité](01-etom-en-pratique.md#exemple-traité)

## 5. Assurance

Travail utilisé ici pour examiner une panne de service et rétablir la capacité attendue. L’exemple de panne data passe de la plainte du client à l’investigation côté service et ressource.

[Module 1 : Exemple traité](01-etom-en-pratique.md#exemple-traité)

## 6. Facturation

Travail qui relie la consommation enregistrée au montant facturé dans notre exemple. Une réparation technique ne décide pas à elle seule d’un ajustement financier.

[Module 1 : Exemple traité](01-etom-en-pratique.md#exemple-traité)

## 7. Passage de relais

Moment où une responsabilité transmet du travail à une autre. Nous vérifions qui prend la suite et quelles informations doivent garder leur sens à cette frontière.

[Module 1 : Pourquoi les couches comptent](01-etom-en-pratique.md#pourquoi-les-couches-comptent)

## 8. Objet métier

Élément dont les équipes doivent parler et qu’elles doivent reconnaître, comme un accord forfait. Son sens et ses relations viennent avant le choix d’une table ou d’un document de stockage.

[Module 2 : Un sens partagé avant le choix du stockage](02-le-sid-en-pratique.md#un-sens-partagé-avant-le-choix-du-stockage)

## 9. Modèle d’information

Description du sens de nos objets et de leurs relations. Elle peut expliquer pourquoi plusieurs préparations se rattachent à un achat sans décider comment les stocker.

[Module 2 : Un sens partagé avant le choix du stockage](02-le-sid-en-pratique.md#un-sens-partagé-avant-le-choix-du-stockage)

## 10. Modèle de données

Choix de stockage qui inscrivent l’information dans une implémentation. Tables, clés et contraintes répondent à d’autres questions que le sens d’un achat ou d’une connexion.

[Module 2 : Un sens partagé avant le choix du stockage](02-le-sid-en-pratique.md#un-sens-partagé-avant-le-choix-du-stockage)

## 11. Produit

Dans notre exercice, vue de ce que l’acheteur a accepté de recevoir. L’accord forfait inventé permet de distinguer cet achat des moyens techniques qui le portent.

[Module 2 : Produit, service et ressource](02-le-sid-en-pratique.md#produit-service-et-ressource)

## 12. Service

Dans notre exercice, capacité qui doit fonctionner pour l’acheteur. La promesse de connexion décrit ce besoin sans le confondre avec une SIM particulière.

[Module 2 : Produit, service et ressource](02-le-sid-en-pratique.md#produit-service-et-ressource)

## 13. Ressource

Dans notre exercice, moyen technique employé pour fournir la capacité. Remplacer la SIM attribuée change ce moyen sans modifier nécessairement l’achat.

[Module 2 : Produit, service et ressource](02-le-sid-en-pratique.md#produit-service-et-ressource)

## 14. Référence

Valeur permettant de reconnaître le même objet au fil des étapes. Notre agreement-A inventé relie préparation et disponibilité à un achat ; ce n’est pas un champ officiel.

[Module 2 : Exemple traité](02-le-sid-en-pratique.md#exemple-traité)

## 15. Bloc fonctionnel

Regroupement de responsabilités utilisé pour discuter de la prise en charge du travail. Notre bureau des commandes est un tel bloc, mais le dessiner n’impose pas une application déployée séparément.

[Module 3 : Trois vues du même relais](03-le-functional-framework-en-pratique.md#trois-vues-du-même-relais)

## 16. Responsable de la décision

Responsabilité qui décide si un résultat peut être annoncé. Dans notre histoire, l’atelier connexion décide de la disponibilité technique et le bureau des nouvelles la communique.

[Module 3 : Exemple traité](03-le-functional-framework-en-pratique.md#exemple-traité)

## 17. Contrat d’interface

Accord sur ce qu’un appelant peut demander et sur la réponse attendue. Il décrit l’échange en laissant distincts les choix de stockage de l’implémentation destinataire.

[Module 4 : Un contrat au passage de relais](04-les-open-apis-en-pratique.md#un-contrat-au-passage-de-relais)

## 18. Implémentation

Logiciel qui réalise effectivement le comportement décrit par un contrat. Deux implémentations peuvent proposer le même échange tout en organisant différemment leur travail interne.

[Module 4 : Un contrat au passage de relais](04-les-open-apis-en-pratique.md#un-contrat-au-passage-de-relais)

## 19. Catalogue

Vue de ce qui pourrait être proposé à un acheteur dans notre exemple. Choisir une offre est différent d’enregistrer le produit finalement détenu par cet acheteur.

[Module 4 : Erreurs à éviter](04-les-open-apis-en-pratique.md#erreurs-à-éviter)

## 20. Inventaire

Vue des instances enregistrées, comme un service ou une ressource attribuée. Lire une fiche n’active pas un équipement et ne prouve pas que la connexion fonctionne.

[Module 4 : Exemple traité](04-les-open-apis-en-pratique.md#exemple-traité)

## 21. Accusé de réception

Réponse indiquant à l’appelant que sa demande a été reçue ou acceptée dans l’échange conçu. Notre exemple exige encore une preuve distincte de disponibilité avant d’annoncer une connexion fonctionnelle à l’acheteur.

[Module 4 : Exemple traité](04-les-open-apis-en-pratique.md#exemple-traité)

## 22. Composant

Frontière logicielle autour de travaux regroupés dans notre conception. Nous décrivons ce que le bureau des commandes possède, expose et consomme avant de choisir son déploiement.

[Module 5 : Donner une frontière aux responsabilités](05-les-composants-en-pratique.md#donner-une-frontière-aux-responsabilités)

## 23. Contrat exposé

Opération qu’un composant met à disposition de ses appelants. Notre opération prepare inventée vérifie la demande et retourne une préparation, pas une connexion active.

[Module 5 : Exemple traité](05-les-composants-en-pratique.md#exemple-traité)

## 24. Dépendance consommée

Autre contrat dont un composant déclare avoir besoin. Le lab 3 vérifie le nom de la dépendance sans appeler de service distant ; la déclaration ne prouve donc pas sa disponibilité.

[Module 5 : Exemple traité](05-les-composants-en-pratique.md#exemple-traité)

## 25. Identité d’événement

Valeur utilisée pour reconnaître plusieurs livraisons d’un même événement. Elle diffère de la référence d’accord, car plusieurs événements légitimes peuvent concerner le même achat.

[Module 6 : Trois façons de perdre le relais](06-assurance-et-facturation-en-pratique.md#trois-façons-de-perdre-le-relais)

## 26. Idempotence

Ici, rejouer le même ajustement conserve un seul effet financier. Le lab 4 le démontre dans un même appel ; redémarrer un processus ne conserve pas sa mémoire.

[Module 6 : Exemple traité](06-assurance-et-facturation-en-pratique.md#exemple-traité)

## 27. Déduplication

Reconnaître qu’un événement a déjà été traité pour ne pas appliquer de nouveau son effet. Ce contrôle seul ne peut pas replacer un ajustement précoce après le rétablissement dont il dépend.

[Module 6 : Trois façons de perdre le relais](06-assurance-et-facturation-en-pratique.md#trois-façons-de-perdre-le-relais)

## 28. Événement hors ordre

Événement reçu avant un prédécesseur requis par notre séquence. L’exercice garde l’ajustement en attente du rétablissement au lieu de prendre l’étape manquante pour une réussite.

[Module 6 : Trois façons de perdre le relais](06-assurance-et-facturation-en-pratique.md#trois-façons-de-perdre-le-relais)

## 29. Événement tardif

Événement reçu longtemps après son occurrence, selon le seuil choisi pour l’exercice. Il est signalé mais peut encore être traité lorsque ses prédécesseurs sont présents.

[Module 6 : Trois façons de perdre le relais](06-assurance-et-facturation-en-pratique.md#trois-façons-de-perdre-le-relais)

## 30. Preuve

Observation ou livrable qui appuie une affirmation précise pendant la revue. Un résultat de rejeu local étaye ce qui s’est passé pendant cette exécution, pas le fonctionnement d’un système déployé chez un opérateur.

[Module 8 : Dix questions de revue](08-projet-de-synthese.md#dix-questions-de-revue)
