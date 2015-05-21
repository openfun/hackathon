---
title: Activités
layout: default
---

# Open edX et les différents types d'activités

Une activité Open edX peut aller de la simple page HTML aux quiz et évaluations par les pairs.

Pour qu'un MOOC ait du succès, il est recommandé de varier les types d'activités afin d'éviter l'aspect répétitif et permettre au cours d'être suivi avec plus d'engagement.

Lorsqu'un type d'activité n'est pas disponible directement dans Open edX, plusieurs options s'offrent aux développeurs pour les y ajouter (nous n'en décrirons que 2 ici):

- Le [Xblock](/hackathon/03a-xblock.html): une extension en python qui doit être installée sur le serveur qui héberge la plateforme. C'est probablement la meilleure solution si vous avez accès au serveur.
- Le JS-Input [JS-Input](/hackathon/03b-js-input.html): probablement moins flexible en terme de possibilités offertes, mais probablement la réponse à de nombreux besoins.  Le JS-Input a l'avantage d'être une extension dont l'installation se fait directement dans un cours sans nécéssiter un accès au serveur.

[Options for Extending the edX Platform](http://edx-developer-guide.readthedocs.org/en/latest/extending_platform/extending.html)
