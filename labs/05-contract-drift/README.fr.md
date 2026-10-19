# Lab 5 – Dérive d’un contrat

[English version](README.md)

Poursuivez le [module 5](../../docs/fr/05-les-composants-en-pratique.md#comparer-deux-déclarations) et le [lab 3](../03-component-contract/README.fr.md). Le bureau des commandes publie deux déclarations inventées. Comparez leurs promesses avant de décider ce qu’un appelant doit réexaminer. Les données et règles ci-dessous appartiennent à cet exercice ; aucun schéma officiel n’est reproduit.

## Exécuter

Python 3.9 ou ultérieur et sa bibliothèque standard suffisent. Depuis la racine du dépôt :

```console
python -X utf8 labs/05-contract-drift/drift.py
python -X utf8 labs/05-contract-drift/drift.py labs/05-contract-drift/drift_samples.json
python -m unittest discover -s labs/05-contract-drift -p test_drift.py
python tools/check_docs.py
```

Le fichier par défaut est trouvé à côté du script, même depuis un autre répertoire courant. Un chemin fourni est relatif au répertoire courant. `-X utf8` conserve la sortie bilingue redirigée en UTF-8, y compris sous Windows. Le script affiche les deux langues ensemble ; les noms des opérations et des champs restent inchangés.

L’exemple produit six constats : un ajout compatible, deux changements à examiner et trois ruptures. Le code 0 signifie que la comparaison est terminée, même en présence d’une rupture. Une entrée invalide ou un fichier illisible produit une erreur bilingue sur stderr et le code 2. Une comparaison vide indique qu’aucun changement déclaré n’a été trouvé ; elle ne revendique aucune compatibilité à l’exécution.

## Lire la déclaration

[drift_samples.json](drift_samples.json) contient exactement `before` et `after`. Chaque déclaration est soit `{}`, soit un objet avec `exposes`, un dictionnaire de noms d’opérations. Chaque opération contient exactement `fields`, un dictionnaire de noms de champs associés à `type` et au booléen `required`. `exposes` et `fields` peuvent être vides. Clés inconnues, noms blancs et structures invalides sont rejetés plutôt qu’ignorés.

Ce format pédagogique distinct s’inspire du lab 3 ; il ne lit pas `describe()` et ne décrit pas un composant complet. Il décrit seulement des champs de requête plats. Il ne contient ni champs retournés, ni dépendances déclarées, ni observations à l’exécution. Ajouter ces clés constitue une erreur d’entrée.

Les types forment le vocabulaire inventé `string`, `integer`, `number`, `boolean`, `null`, `array` et `object`. Une liste non vide représente des alternatives, par exemple `["string", "null"]`. Types inconnus et alternatives dupliquées sont rejetés. Ici, `number` inclut `integer` ; aucune autre inclusion n’est déduite. L’ordre de la liste ne compte pas et `number` équivaut à `["integer", "number"]`. Les éléments de tableaux et les propriétés d’objets ne sont pas décrits.

## Règles de classement

La comparaison va de l’ancienne déclaration à la nouvelle. Ce sont les règles de revue de ce lab, pas une politique universelle de compatibilité.

| Changement déclaré | Classement | Lecture |
|---|---|---|
| Champ optionnel ajouté | compatible | La nouvelle déclaration n’exige pas que l’appelant le fournisse |
| Champ obligatoire ajouté ou champ optionnel devenu obligatoire | à examiner | Identifier les appelants qui peuvent l’omettre avant de décider de la migration |
| Champ obligatoire devenu optionnel | compatible | La déclaration accepte son omission |
| Type élargi à un sur-ensemble strict | à examiner | Examiner le sens des valeurs désormais acceptées |
| Type changé ou restreint | rupture | Des valeurs précédemment acceptées peuvent être exclues |
| Champ obligatoire retiré | rupture | Le lab traite le retrait d’un champ obligatoire promis comme une rupture |
| Champ optionnel retiré | à examiner | Vérifier si les appelants l’envoient encore ou en dépendent |
| Opération retirée | rupture | Les appelants perdent une opération |
| Opération ajoutée | compatible | Les opérations existantes restent disponibles dans la déclaration |

Passer de `string` à `["string", "null"]`, ou d’`integer` à `number`, est un élargissement. Passer de `string` à `integer`, ou de `number` à `integer`, est une rupture selon ces règles. À examiner ne signifie pas sans risque : rendre un champ obligatoire peut déjà casser un appelant ; une personne doit donc examiner les usages.

Chaque constat porte un `code` stable, une `classification`, un chemin sous forme de liste de clés et `message.en` / `message.fr`. Opérations et champs sont parcourus dans l’ordre trié. Une opération ajoutée ou retirée est signalée une fois à sa frontière, sans répéter les constats sur ses champs. Un champ conservé dont le type et le caractère obligatoire changent produit deux constats. Des déclarations de type équivalentes n’en produisent aucun. `compare(before, after)` retourne une liste sans modifier ses arguments.

## Essayer et expliquer

1. Prévoyez les six constats avant d’exécuter l’exemple. Retrouvez chaque clé modifiée dans les deux déclarations.
2. Dans une copie jetable, remettez `quantity` à `integer`. Le constat d’élargissement doit disparaître.
3. Rendez `comment` obligatoire. Expliquez pourquoi il faut désormais l’examiner plutôt que déclarer l’appelant à l’abri.
4. Donnez à un champ le type `mystery`. Toute la comparaison doit échouer, même si son opération est ajoutée ou retirée.
5. Gardez deux déclarations identiques, mais imaginez que l’implémentation applique deux fois un ajustement. Expliquez pourquoi cette comparaison ne voit aucun changement, puis utilisez le [lab 4](../04-event-trace/README.fr.md) pour raisonner sur les effets observables.

## Ce que la comparaison ne voit pas

Une déclaration peut rester identique alors que le code cesse de la respecter. Le script n’appelle aucune opération et ne teste ni réponses, persistance, concurrence, authentification, délais, ordre des événements ou idempotence. Il ne prouve ni l’existence d’une dépendance, ni la fin d’une réparation, ni l’application unique d’un ajustement. Le [module 6](../../docs/fr/06-assurance-et-facturation-en-pratique.md) sépare ces preuves manquantes du contrat déclaré.

Les 17 tests couvrent déclarations vides et identiques, toutes les règles de classement, équivalence des types, changements multiples d’un champ, validation des entrées, types inconnus, arguments inchangés et ligne de commande. Ils établissent uniquement le comportement de cet exercice local. Aucune donnée client réelle, appel réseau, mise en production, évaluation de conformité ou de certification. Voir la [notice](../../NOTICE.fr.md).
