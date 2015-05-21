---
title: Activités
layout: default
---

# Open edX et les différents types d'activités

Une activité Open edX peut aller de la simple page HTML aux quiz et évaluations par les pairs.

Bien l'offre soit assez vaste, "beaucoup" n'est souvent pas assez pour l'ensemble des acteurs de la plateforme.

Pour répondre à la demande des MOOC, il faut souvent créer de multiple types
d'activités afin d'éviter l'aspect répétitif et permettre au cours d'être suivi avec plus d'engouement. Il ne faut pas être limité à un choix toujours trop
réduit de types de quiz.

Open edX propose de résoudre ce problème en mettant à portée du
développeur/concepteur deux technologies:

- Le [Xblock](#xblocks): une extension en python qui doit
être installée sur le serveur qui héberge la plateforme. C'est probablement la
meilleure solution si vous avez accès au serveur.
- Le JS-Input [JS-Input](#js-input): probablement moins flexible en terme de possibilités offertes, mais
probablement la réponse à de nombreux besoins.  Le JS-Input a l'avantage d'être
une extension dont l'installation se fait directement dans un cours sans
nécéssiter un accès au serveur.
