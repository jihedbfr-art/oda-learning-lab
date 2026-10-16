# Lab 1 – La portabilité du numéro comme processus

[English version](README.md)

Lab communautaire non officiel. Prérequis : [module 1 – eTOM en pratique](../../docs/fr/01-etom-en-pratique.md). Données synthétiques uniquement. Rien ici ne certifie une conformité TM Forum.

## Sources et prérequis

Ce guide s’appuie sur le [README public](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/README.md), le [modèle du processus](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/src/main/resources/processes/number-portability-saga.bpmn) et la [configuration de compilation](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/pom.xml) à la révision `9d1bf041bdf051586ba1edfda320649b925d2e5a`, consultés le 2026-10-16. La correspondance proposée ci-dessous est notre interprétation.

Pour Docker, prévoyez Git, Docker avec Compose et les ports locaux 8080, 9092, 16686 et 4318 disponibles. La voie Maven demande Java 17 et Maven, selon la configuration et les commandes du README. Les téléchargements d’images, le stockage et le calcul consomment des ressources locales ; aucun service cloud payant n’est nécessaire. Les volumes à télécharger et les besoins matériels n’ont pas été mesurés.

## Récupérer et lancer le lab

Utilisez le menu **Code** du dépôt source pour obtenir un clone local, puis placez-vous à sa racine. Son README ne fournit pas de commande de clonage ; ce guide n’en invente donc pas. Vérifiez la révision pour retrouver exactement les fichiers liés ci-dessus.

Voici les commandes exactes de la section Quick start, pour un shell compatible Bash :

```bash
cp .env.example .env
docker compose up -d
```

Ouvrez Cockpit sur `http://localhost:8080/camunda` et Jaeger sur `http://localhost:16686`. Consultez le dépôt source pour les paramètres d’accès de développement local ; n’utilisez aucun accès client ou de production. Le README propose aussi cette alternative :

```bash
mvn spring-boot:run
```

Cette alternative utilise une base en mémoire et perd son état au redémarrage. Elle ne démarre pas Kafka pour vous. Lisez la section Running it avant de la choisir ; elle ne valide pas à elle seule la livraison par le broker.

Pour créer une demande et envoyer une décision du donneur, suivez les exemples HTTP exacts de [Quick start](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/README.md#quick-start). Restez sur localhost avec des données synthétiques. Relevez la référence renvoyée et remplacez le paramètre de l’URL de réponse ; garder le paramètre littéral ne cible pas votre instance. Aucun message ne doit atteindre un opérateur réel.

## Suivre le processus avant de le classer

Suivez les identifiants d’activités du modèle, sans déduire un ordre à partir du framework métier :

1. `validateRequest` contrôle la demande, puis `notifyDonor` demande la notification du donneur.
2. `awaitDonorResponse` contient l’événement d’attente de message. Son timer interruptif de bordure `slaTimeout` quitte l’attente si aucune réponse n’arrive à temps.
3. Une acceptation passe par `activateOnRecipient`, `notifyCompletion`, puis la fin `completed`.
4. Un refus et une expiration rejoignent `compensateProvisioning`, puis la tâche humaine `manualReview`. La fin `rejected` arrive **après** la clôture de cette tâche, pas simplement après la compensation.

Commencez par l’acceptation. Recommencez avec un refus, puis sans réponse. Pour chaque cas, relevez l’activité courante, la référence de demande et la preuve observée. Lisez le délai configuré sans le prendre pour une obligation réglementaire. Aucun SLA propre à un pays n’est établi ici.

## Votre correspondance

Avant de lire l’exemple, remplissez une ligne par activité : **étape du processus → domaine métier agissant → flux (fulfilment / assurance / billing)**. Ajoutez l’objet entrant, l’objet sortant et une phrase justifiant votre choix. Utilisez les domaines généraux du module 1 ; n’inventez aucun code eTOM officiel.

### Exemple de réponse possible

Cette proposition est discutable ; ce n’est pas un corrigé officiel. Le domaine décrit une responsabilité dans l’histoire, pas le nom d’un composant logiciel.

| Étape du processus | Domaine métier agissant | Flux | Raisonnement |
|---|---|---|---|
| Valider la demande | Client | Fulfilment | Vérifier le changement demandé avant sa réalisation |
| Notifier le donneur | Service, puis partenaire | Fulfilment | Demander à un autre opérateur de coordonner le changement |
| Attendre la réponse / expiration SLA | Partenaire et service | Fulfilment | Attendre un préalable à l’achèvement de la demande |
| Activer chez le receveur | Service / ressource | Fulfilment | Représenter l’étape de réalisation technique |
| Notifier la fin | Client | Fulfilment | Annoncer le résultat du changement demandé |
| Compenser | Service / ressource | Fulfilment | Récupérer après une tentative de fourniture infructueuse |
| Revue manuelle | Client / partenaire | Fulfilment ; assurance défendable si traitement d’un incident de service | Une personne examine pourquoi la demande n’a pas abouti |

Un timer ne signifie pas automatiquement assurance. Ici, il encadre une demande de fourniture inachevée. Ce processus ne démontre aucune facturation ; laissez ce flux absent au lieu de forcer tous les flux dans le tableau.

## Objets aux passages de relais

Suivez accueil client → orchestration → frontière donneur → étape receveur → information client. Inventez des noms comme « note de transfert », « réponse du donneur » et « avis de résultat ». Reliez-les par la même référence de demande. Ce sont des objets d’exercice, pas des classes SID ni des messages standard.

À chaque relais : qui porte l’action suivante, quelle information doit survivre, quelle preuve établit la réception ? Distinguez une notification demandée d’une notification livrée. Gardez cette liste pour l’exercice du module 2 sur le modèle d’information. Dessinez vous-même les relations et expliquez comment distinguer une réponse tardive d’une réponse actuelle.

## Contrôles et limites

Le README source documente ces commandes de test :

```bash
mvn test       # process tests against the embedded H2 engine — no Docker
mvn verify     # also runs the Testcontainers check against a real Kafka broker and a PostgreSQL database
```

Vérification locale le 2026-10-16, révision ci-dessus : `mvn test` réussi, 12 tests, aucun échec, erreur ou test ignoré (dont les quatre chemins de portabilité). Seuls les tests embarqués ont été exécutés ; le lab interactif Docker/Cockpit n’a pas été lancé. `mvn verify` et les intégrations Testcontainers n’ont pas été exécutés.

Les tests embarqués du processus vérifient acceptation, refus, expiration et entrée invalide. Leur publication d’événements est simulée ; le test d’expiration avance l’horloge du moteur et déclenche son job de timer. Ce n’est pas une mesure du temps réel ni de livraison par le broker.

Le lab démontre un processus exécutable avec délai et branche de compensation dans le périmètre testé. Ses [délégués d’activation](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/src/main/java/com/jihedapps/provisioning/delegate/ActivateOnRecipientDelegate.java) et de [compensation](https://github.com/jihedbfr-art/bpmn-provisioning-patterns/blob/9d1bf041bdf051586ba1edfda320649b925d2e5a/src/main/java/com/jihedapps/provisioning/delegate/CompensateProvisioningDelegate.java), lus le 2026-10-16, publient des événements ; ils n’activent ni n’annulent une configuration réseau réelle. La compensation est ici une tâche de service, pas une preuve de la sémantique des événements BPMN de compensation.

Il ne démontre ni conformité TM Forum, ni Open API standard, ni intégration réelle entre opérateurs, ni conformité réglementaire, ni test sur données clients réelles. Conservez votre journal d’exécution séparément de cette proposition de correspondance.
