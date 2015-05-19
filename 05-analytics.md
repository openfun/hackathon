---
title: Analytics
layout: default
---

# Analytics {#analytics}

## Introduction

FUN met à la disposition des participants au hackathon une quantité de logs
extraits de ses machines de productions à fins d'analyse. 

## Téléchargement des fichiers de logs

TODO

## Source des logs

Les logs proviennent des appels à `tracker.emit` qui parsèment le code d'edX et
de FUN :
https://github.com/edx/event-tracking/blob/0.2.0/eventtracking/tracker.py#L65

Chaque évènement loggé se présente sous la forme d'un blob JSON contenant au
moins un champ `time`.
    
## Format des logs

Les logs fournis par FUN sont anonymisés, ce qui signifie que les champs
`email`, `address`, etc. ont été retirés des blobs JSON. Par ailleurs, le
champs `username` a été chiffré à l'aide d'une méthode de chiffrage à sens unique :

    encrypted_username = hmac.new(secret_key, username, hashlib.sha256).hexdigest()

## Analyse des logs à l'aide de ElasticSearch

Les logs fournis par FUN se prêtent particulièrement bien à l'analyse via
ElasticSearch. Si vous décidez de charger les logs fournis dans un cluster
ElasticSearch, nous vous recommandons d'installer la pile ELK : ElasticSearch +
Logstash + Kibana.

* ElasticSearch est le moteur d'indexation et de recherche de vos données.
* Kibana est le frontend qui vous permettra de visualiser vos données dans le navigateur.
* Logstash permet d'envoyer vos logs à ElasticSearch en les convertissant en évènements au format ad-hoc.

### Installation

L'installation des trois composants de la stack ELK est bien documentée :

* https://www.elastic.co/downloads/elasticsearch
* https://www.elastic.co/downloads/logstash
* https://www.elastic.co/downloads/kibana

### Envoi des logs vers ElasticSearch

Une fois que vous avez correctement installé Logstash et ElasticSearch, vous
pouvez insérer les logs de FUN dans ElasticSearch à l'aide du fichier de
configuration `logstash.conf` fourni dans ce dépôt :

    cat fun_tracking_logs.log | logstash --config static/logstash.conf

### Visualisation des résultats dans Kibana

Après avoir inséré quelques évènements dans ElasticSearch, vous pouvez lancer
Kibana et observer ces évènements en ouvrant
[http://localhost:5601](http://localhost:5601) dans votre navigateur. N'oubliez
pas de sélectionner un intervalle de temps couvert par
les logs (en haut à droite).

### Réaliser des requêtes manuelles sur ElasticSearch

Vous pouvez souhaiter réaliser des requêtes complexes sur ElasticSearch et en
récupérer le résultat brut au format JSON sans passer par Kibana. Pour ça, le
mieux est de :

1. créer une requête via Kibana, dans l'onglet "Discover".
2. récupérer cette requête au format JSON, en repliant le graphe de résultats, puis sous l'onglet "Request". Par exemple :
    
    {
      "size": 500,
      "sort": {
        "@timestamp": "desc"
      },
      "query": {
        "filtered": {
          "query": {
            "query_string": {
              "query": "*",
              "analyze_wildcard": true
            }
          }
        }
      }
    }

3. Copier-coller cette requête dans un fichier `query.json`, puis réaliser la requête à l'aide du script fourni dans ce dépôt :

    static/es.py query.json > result.json
