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

    sudo apt-get install python python-pip python-virtualenv git make g++ vagrant ansible

Une autre façon d'installer pip consiste à télécharger le script `https://bootstrap.pypa.io/get-pip.py`:

    wget https://bootstrap.pypa.io/get-pip.py -P /tmp/ && sudo python /tmp/get-pip.py

Il est nécessaire d'avoir la version >= 1.5.3 de Vagrant. Si la version
présente dans les dépôts de votre distribution n'est pas suffisamment récente,
vous pouvez la mettre à jour à partir de
[http://www.vagrantup.com/downloads](la page téléchargement de Vagrant).

De même, si vous ne disposez pas de la version la plus récente de Virtualbox,
vous pouvez la télécharger à partir
[d'ici](https://www.virtualbox.org/wiki/Linux_Downloads).

Vous allez également avoir besoin des *Vagrant guest additions*:

    vagrant plugin install vagrant-vbguest
