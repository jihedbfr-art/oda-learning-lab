# Lab 2 – Un petit catalogue produit

[English version](README.md)

Cet exercice original reprend le forfait mobile du [module 2](../../docs/fr/02-le-sid-en-pratique.md). Travaillez seul, hors ligne, avec quatre offres inventées. Les données ne contiennent aucun client, abonnement ou équipement réseau.

## L'idée

Une offre décrit ce qui peut être choisi. Une spécification décrit les capacités réutilisables derrière ce choix. Un prix décrit le montant de l'exercice. Deux offres peuvent réutiliser les mêmes capacités avec des montants différents. Ce modèle pédagogique est le nôtre ; aucun schéma officiel n'est reproduit.

Lisez [catalog.json](catalog.json). Son premier champ `notice` indique dans les deux langues que toutes les données sont synthétiques. `credits` est une unité inventée, ni une devise ni un tarif commercial. `month` est la période commune de comparaison. Aucun calcul de taxe, de consommation ou de remise n'est sous-entendu.

| Objet | Champs propres | Sens dans cet exercice |
|---|---|---|
| Spécification | `id`, `services` | Une liste réutilisable de capacités |
| Offre | `id`, `name` bilingue, `specification` | Un choix lié à une spécification |
| Prix, dans une offre | `credits`, `period` | Un nombre entier positif ou nul de crédits par mois |

`voice` désigne les appels et `mobile-data` la connexion mobile dans cette histoire. Ces libellés sont inventés. Une spécification réutilisable n'est pas un service activé pour un acheteur précis.

## Exécuter

Prérequis : Python 3. Aucune installation de paquet, aucun compte, serveur ou accès réseau. Depuis la racine du dépôt :

```console
python labs/02-product-catalog/catalog.py
python -m unittest discover -s labs/02-product-catalog -p test_catalog.py
python tools/check_docs.py
```

Le script lit toujours le JSON placé à côté de lui, quel que soit le répertoire courant. Il affiche les liens et n'écrit aucun fichier. Sortie relevée le 16 octobre 2026 avec Python 3.12.0 :

```text
Synthetic data / Données synthétiques
Valid offers / Offres valides: 4
offer-A | spec-talk | voice | 8 credits/month (crédits/mois)
offer-B | spec-data | mobile-data | 12 credits/month (crédits/mois)
offer-C | spec-mix | voice, mobile-data | 18 credits/month (crédits/mois)
offer-D | spec-mix | voice, mobile-data | 15 credits/month (crédits/mois)
```

Six tests unitaires ont réussi. Ils vérifient le catalogue fourni, une référence de spécification absente, les identifiants d'offre dupliqués, les montants invalides, les noms bilingues absents ou vides et les structures de collections invalides. Ces tests protègent les liens et les montants utilisés dans l'exercice. La validation applique ces contraintes pédagogiques, pas un schéma JSON complet ; le lecteur examine la notice et les noms bilingues. Une entrée mal formée ou illisible produit une erreur bilingue et un code de sortie 1.

## Exercice guidé

1. Dessinez vos propres boîtes pour une offre, une spécification et un prix. Nommez leurs liens. Quels objets sont réutilisés ?
2. Prévoyez quelles offres contiennent la connexion mobile avant de lancer le script. Suivez chaque référence au lieu de déduire la réponse des noms.
3. Comparez C et D. Expliquez pourquoi des prix différents ne demandent pas forcément des spécifications différentes. Aucune règle d'éligibilité ou de promotion n'est encodée.
4. Dans une copie jetable, ajoutez une cinquième offre avec des noms bilingues, réutilisez `spec-data` et choisissez un montant entier de crédits inventés. Exécutez et expliquez la ligne ajoutée. Restaurez les données fournies avant leurs tests, qui attendent quatre offres.
5. Dans cette copie, essayez une référence de spécification inconnue, puis un montant négatif. Exécutez après chaque changement, notez le rejet et restaurez le fichier.
6. Revenez au relais de commande du module 2. Quelle référence d'offre choisie transmettriez-vous dans l'accord forfait inventé ? Que manquerait-il encore pour activer un service ?

## Une lecture possible

B, C et D contiennent la connexion mobile ; A non. C et D partagent `spec-mix` et ses deux capacités. Leur différence est de 3 crédits inventés par mois. Cette comparaison n'est pas une facture : aucun client n'a acheté ces offres.

## Vérifiez-vous et limites

Savez-vous distinguer une spécification réutilisable d'un service actif ? Quel problème une référence inconnue causerait-elle au relais ? Pourquoi des services identiques ne prouvent-ils pas des conditions commerciales identiques ?

Le script exécuté démontre la lecture locale, la validation des liens et l'affichage de données synthétiques. Il n'implémente aucune API réelle et ne démontre aucune conformité TMF620. Aucune spécification ou charge utile n'est copiée. Il ne gère ni commande, persistance, activation, moteur de facturation ou sécurité, et ne fournit aucune preuve de performance. L'exécution utilise uniquement votre machine et n'appelle aucun service payant. Voir la [notice](../../NOTICE.fr.md).
