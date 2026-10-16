# Module 6 – Assurance et facturation en pratique

[English version](../en/06-assurance-and-billing-in-practice.md)

Ressource communautaire non officielle, sans lien avec TM Forum. Prérequis : [module 2](02-le-sid-en-pratique.md), [module 3](03-le-functional-framework-en-pratique.md), [module 4](04-les-open-apis-en-pratique.md) et [module 5](05-les-composants-en-pratique.md). Cette suite du forfait mobile est inventée, sans étude d'opérateur réel.

## Suivre les preuves après la réparation

La data mobile cesse de fonctionner après l'activation. Le support enregistre une note de panne liée à la promesse de connexion. L'atelier connexion examine le kit attribué, rétablit la connexion et transmet ses preuves. Le bureau des frais propose ensuite un ajustement de la feuille de calcul des frais. Réparer la connexion et ajuster la facture sont deux décisions avec des responsables distincts.

L'ajustement vaut ici trois crédits inventés. Ce n'est ni un tarif ni un droit à indemnisation. Une politique réelle, une approbation et un traitement comptable demanderaient leurs propres preuves ; rien n'est déduit d'un rétablissement technique.

## Garder ensemble objets, blocs et contrats

| Relais | Objets du module 2 | Blocs du module 3 | Contrat inventé et responsable |
|---|---|---|---|
| Signaler | Note de panne, accord forfait | Bureau des pannes | Enregistrer l'accord touché ; ce bureau possède l'investigation |
| Examiner | Promesse de connexion, kit attribué | Atelier connexion, réserve de kits | Retourner un diagnostic rattaché au même incident |
| Rétablir | Promesse de connexion, note de panne | Atelier connexion, bureau des nouvelles | Transmettre la preuve ; l'atelier décide de la disponibilité technique |
| Ajuster | Feuille de frais, accord forfait, note de panne | Bureau des frais | Appliquer un ajustement approuvé ; ce bureau possède le montant |
| Relire | Trace d'ajustement, note de panne | Bureaux des pannes et des frais | Confirmer la complétude avant de terminer la revue |

Objets et contrats sont pédagogiques. La distinction entre contrat et implémentation du module 4 reste utile. Le module 5 ajoute les dépendances déclarées : le bureau des frais ne peut pas dépendre silencieusement d'un signal de réparation que personne ne promet de livrer. Conservez une référence d'incident et d'accord à chaque relais.

## Trois façons de perdre le relais

Un doublon d'ajustement peut créditer deux fois. Le consommateur a besoin d'une identité stable d'événement et doit rejeter un contenu contradictoire sous la même identité. Dédupliquer en mémoire sert ici à raisonner ; un traitement durable demanderait aussi de décider des écritures atomiques et de la reprise après arrêt.

Un événement hors ordre arrive avant son prédécesseur. Dans le [lab 4](../../labs/04-event-trace/README.fr.md), l'ajustement arrive avant le rétablissement. Le traitement ordonné le garde en attente jusqu'à la séquence deux. Cela préserve la dépendance ; dédupliquer seul ne suffirait pas. Sans rétablissement, le trou reste visible et ne devient pas une réussite.

Un événement tardif présente un grand écart entre occurrence et réception. Notre seuil inventé est de dix unités de temps logique. La revue arrive treize unités après son occurrence. Elle est signalée puis traitée quand ses prédécesseurs sont présents. Cette règle n'impose aucun SLA opérationnel. Ordre de réception, ordre des séquences et date d'occurrence répondent à des questions différentes.

## Exemple traité

Lisez les cinq enregistrements JSON dans l'ordre du fichier. Ouverture : séquence un. Ajustement : trois. Rétablissement : deux. L'ajustement est ensuite livré une seconde fois. La revue porte la séquence quatre et arrive tard. Le traitement naïf additionne les deux livraisons : six crédits. Le traitement idempotent et ordonné produit trois crédits et applique ouverture, rétablissement, ajustement puis revue.

Rejouez toute la liste deux fois dans un même appel. Le traitement ordonné conserve un seul effet financier. Un nouveau processus repart sans mémoire : ce lab n'est pas un service de déduplication durable. Retirez le rétablissement : les séquences trois et quatre restent en attente, sans ajustement appliqué.

## Erreurs à éviter

- Fermer la note de panne dès la réparation sans vérifier le relais financier restant.
- Prendre la référence d'accord pour l'identité d'événement : plusieurs événements légitimes concernent le même accord.
- Supprimer tout message tardif : le retard ne prouve pas que le fait métier est faux.
- Revendiquer une livraison unique parce qu'un rejeu local donne le total attendu.

## Exercice

Exécutez les deux modes, expliquez chaque diagnostic puis retirez le rétablissement dans une copie jetable. Nommez le responsable de l'enquête sur le message manquant. Décrivez ensuite un arrêt entre l'écriture de l'ajustement et la mémorisation de son identité. Quelles opérations faut-il rendre atomiques dans une implémentation durable ?

## Vérifiez-vous

- Quels objets relient réparation, achat et feuille de frais ?
- Pourquoi déduplication et ordre répondent-ils à des problèmes différents ?
- Quelle preuve manque encore quand la liste des trous est vide ?

## Limites de ce module

Aucune facturation réelle, donnée client ou intégration réseau. Séquences et ajustements sont inventés, pour un incident par trace. Aucun schéma officiel, conformité TM Forum ou niveau de service revendiqué. Les affirmations sur les frameworks restent limitées à la [matrice datée](../../sources/source-matrix.fr.md) ; cet exemple n'ajoute aucune affirmation sur un tiers.
