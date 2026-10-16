# Lab 3 – Un contrat de composant

[English version](README.md)

Reprenez le forfait mobile synthétique du [module 5](../../docs/fr/05-les-composants-en-pratique.md). Le bureau des commandes annonce ses responsabilités et ses contrats exposés et consommés par `describe()`. Ces dictionnaires sont inventés ; ils ne constituent aucun manifeste officiel.

## Exécuter

Python 3 et sa bibliothèque standard suffisent. Depuis la racine du dépôt :

```console
python labs/03-component-contract/component.py
python -m unittest discover -s labs/03-component-contract -p test_component.py
python tools/check_docs.py
```

Exécution locale le 2026-10-16 : le script a affiché sa déclaration et retourné `{"agreement": "agreement-A", "state": "prepared"}`. Huit tests ont réussi : déclaration, résultat valide, chaque champ absent, types incorrects et valeurs vides, dépendance non déclarée, dépendance manquante, collections invalides et champs supplémentaires, isolation des modifications.

## Essayer la frontière

Prévoyez le résultat avant de modifier une copie jetable de la demande :

1. Retirez `agreement` : la préparation doit échouer.
2. Remplacez `offer` par l'entier `7` : la préparation doit échouer.
3. Ajoutez `charge-desk` aux dépendances : la préparation doit échouer.
4. Retirez `offer-shelf` : la dépendance obligatoire manque.
5. Restaurez les deux références non vides et la dépendance déclarée. La préparation retourne le même accord.

`prepare(request, dependencies)` accepte exactement les champs annoncés. Les dépendances forment un ensemble de noms déclarés ; l'ensemble fourni doit correspondre aux dépendances consommées. Chaque appel à `describe()` retourne un nouveau dictionnaire : modifier un résultat ne change pas les déclarations suivantes.

## Lire le résultat avec précision

`prepared` signifie que la demande a passé la validation, sans activation réseau. `read-offer` est une opération annoncée, sans consultation de catalogue. Le lab vérifie des noms, pas la disponibilité distante ni l'existence d'une offre. Aucun réseau, stockage, calcul de facture ou déploiement. Toutes les références sont synthétiques. Authentification, concurrence et conformité officielle ne sont pas évaluées. Coût : exécution locale sans service payant. Voir la [notice](../../NOTICE.fr.md).
