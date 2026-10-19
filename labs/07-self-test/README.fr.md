# Auto-évaluation des modules

[English version](README.md)

Ce n'est pas un simulateur d'examen officiel. Trente-trois questions originales en français et trente-trois en anglais portent uniquement sur les modules 1 à 6 de ce dépôt. Aucun contenu de question d'examen utilisé. Voir le [module 7](../../docs/fr/07-preparer-les-certifications.md).

## Exécuter

Python 3.9 ou ultérieur, bibliothèque standard uniquement. Depuis la racine :

```console
python labs/07-self-test/quiz.py --lang fr --count 5
python labs/07-self-test/quiz.py --lang en --count 5
python labs/07-self-test/quiz.py --lang fr --count 33 --seed 7 --show-answers
python -m unittest discover -s labs/07-self-test -p test_quiz.py
python tools/check_docs.py
```

Le mode interactif attend votre réponse avant de révéler une correction proposée et la référence module/section. Il ne note pas le texte saisi. `--show-answers` affiche directement les corrections pour une lecture ou une vérification non interactive. `--seed` rend le tirage reproductible dans le même environnement Python ; le tirage ne contient aucun doublon.

## Lire et vérifier la banque

[questions.fr.csv](questions.fr.csv) et [questions.en.csv](questions.en.csv) partagent les identifiants, cinq par module et trois sur la dérive de contrat du module 5. Colonnes : `id`, `question`, `answer`, `module`, `section`. Le module est un chemin relatif à la racine ; la section est son titre exact. Le chargement vérifie colonnes, champs non vides, identités uniques, au moins trente questions, existence des modules et titres dans la langue choisie.

Exécuté le 2026-10-16 : six tests réussis. À cette date chaque banque contenait trente questions ; corrections et références des soixante questions affichées dans les deux langues. Mode interactif vérifié avec une réponse synthétique dans chaque langue. Tests : paires de questions, tirage unique et reproductible, tirage complet, compte invalide, langue inconnue et références ou identités invalides.

## Travailler une réponse

Expliquez d'abord le cas sans aide, comparez à la correction puis relisez la section citée. Notez en privé la distinction oubliée et réessayez sur un autre exemple. Aucune mesure de préparation à une certification officielle ne découle du nombre de bonnes réponses.

## Limites

Aucun réseau, paquet externe, compte ou coût de service. Aucune donnée personnelle enregistrée : les réponses interactives ne sont pas écrites sur disque par le script. L'existence d'une section est vérifiée automatiquement ; l'adéquation de la correction demande une relecture humaine. Aucun programme officiel, prix, barème, promesse de réussite ou contenu protégé. Voir la [notice](../../NOTICE.fr.md).

Ajout le 2026-10-19 : trois questions jumelles sur les règles du lab 5, les types élargis et les preuves d’exécution. Chaque banque contient maintenant 33 questions. Relancez les commandes ci-dessus pour la banque actuelle.
