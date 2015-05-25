---
title: Bienvenue
layout: default
---

# Bienvenue {#bienvenue}

Ceci est la documentation technique relative au Hackathon [#OpenedXHack](http://hack.openedx.fr/) organisé
conjointement par [edX](http://openedx.org/), [France Université
Numérique](http://france-universite-numerique-mooc.fr/) et
[IONISx](https://ionisx.com/) pour imaginer le MOOC de demain. Au boulot :)

{% include toc.html %}

## Note

Les instructions données dans cette documentation sont valables pour une
machine hôte sous Ubuntu >= 12.04. N'hésitez pas à proposer des [pull
requests](https://github.com/openfun/hackathon) pour généraliser les
instructions à d'autres environnements.

## Préliminaires

Vous allez très probablement avoir besoin d'un certain nombre de logiciels que voici :

    sudo apt-get install python python-pip python-virtualenv git make

Une autre façon d'installer pip consiste à télécharger le script `https://bootstrap.pypa.io/get-pip.py`:
 
    wget https://bootstrap.pypa.io/get-pip.py -P /tmp/ && sudo python /tmp/get-pip.py
