# Lab 4 – Une trace d'événements

[English version](README.md)

Suite du [module 6](../../docs/fr/06-assurance-et-facturation-en-pratique.md). Données synthétiques uniquement, aucune conformité TM Forum ni système réel.

## Exécuter

Python 3 standard, sans réseau ni paquet externe. Depuis la racine :

```console
python labs/04-event-trace/event_trace.py
python -m unittest discover -s labs/04-event-trace -p test_trace.py
python tools/check_docs.py
```

Exécuté le 2026-10-16 : dix tests réussis. Le mode naïf produit 6 crédits inventés, le mode idempotent et ordonné 3. Les deux affichent le doublon `credit-A`, le hors ordre `restore-A` et le tardif `review-A`. La sortie porte des libellés EN/FR ; les jetons d'événement ne sont pas traduits.

## Lire le fichier

[events.json](events.json) est lu à côté du script, même depuis un autre répertoire courant. L'ordre du fichier représente les livraisons. `sequence` est l'ordre métier inventé pour un incident ; `occurred` et `received` sont des entiers de temps logique, pas des horodatages réels. Un retard strictement supérieur à dix unités est signalé. L'identité du doublon reste stable ; seule la réception peut changer.

Le mode naïf additionne les montants dans l'ordre fourni sans vérifier les transitions métier. Le mode ordonné impose ouverture, rétablissement, ajustement puis revue, déduplique par identité et attend les séquences manquantes. Il rejette les identités contradictoires et les séquences partagées par plusieurs événements. Tout trou apparaît dans `pending`. La validation de structure reste active dans les deux modes.

## Essayer et expliquer

1. Prévoyez les deux totaux avant d'exécuter.
2. Retirez le rétablissement d'une copie des données. Les séquences 3 et 4 restent en attente, sans crédit.
3. Dans un appel Python, comparez `replay(events)` et `replay(events + events)` : le traitement ordonné garde un seul effet.
4. Modifiez le montant du doublon : la contradiction doit être rejetée.
5. Expliquez quel responsable du module 6 traite le trou et comment prouver le relais vers la facture.

## Limites

Dix tests couvrent doublon, désordre, retard, rejeu, trou, contradiction, structure, séquence dupliquée et absence de mutation. La mémoire est recréée à chaque appel : aucune déduplication durable, transaction, panne réseau, persistance, sécurité ou livraison unique n'est démontrée. Un incident et un accord par trace. Aucune devise réelle ; aucun coût de service. Une trace incomplète retourne les attentes sans prétendre avoir fini ; une entrée invalide affiche une erreur bilingue et retourne 1. Voir la [notice](../../NOTICE.fr.md).
