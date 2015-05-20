---
title: XBlocks
layout: default
---

# Mon premier Xblock 'Hello Student!' {#xblocks}

Les XBlocks enrichissent les contenu de cours : il existe des XBlock pour afficher des vidéos dans le cours, pour y insérer des quiz, pour permettre des discussions de forum, ou même pour exécuter des lignes code. Edx met à disposition un SDK qui aide à la création de XBlocks. Ainsi, il est possible commencer le développement de vos modules XBlock sans avoir à installer la platforme Edx.

Vous trouverez dans ce guide, les instructions pour installer le SDK et pour créer votre premier XBlock.

## Installer le xblock sdk depuis le dépot Github

Création de l'environnement virtuel :

    mkdir venvs/
    virtualenv venvs/xblock-sdk
    source venvs/xblock-sdk/bin/activate

Installation du xblock sdk :

    git clone https://github.com/edx/xblock-sdk.git
    cd xblock-sdk/
    make install
    python manage.py syncdb

## Lancer le serveur de développement

    python manage.py runserver 0.0.0.0:8001

Maintenant depuis votre navigateur allez à cette adresse 127.0.0.1:8001.
Si tout va bien la page suivante devrait apparaître :

![](http://opencraft.com/doc/edx/xblock/_images/workbench_home.png "Optional title")

## Créons la structure de notre xblock

    python script/startnew.py 

Le script demande d'abord un nom court pour notre xblock, choisissons 'hellostudent'.
Ensuite rentrons le nom de classe 'HelloStudentXBlock'

Nous avons maintenant un dossier 'hellostudent' contenant la structure du XBlock.

## Afficher 'Hello student'

Ouvrons le fichier `hellostudent/static/html/hellostudent.html` et remplaçons son contenu par :


    <div class="hellostudent_block">
        <p>Hello Student !</p>
    </div>

## Enregistrer notre xbock dans le workbench.

Pour afficher notre xblock il est nécessaire de l'installer dans l'environnement de travail, le 'workbench'. L'installation est contrôlée par le fichier `setup.py` qu'il faudra modifier pour l'adapter à nos besoins.

    # Se mettre dans l'environnement virtuel avant l'installation du paquet.
    cd hellostudent/
    pip install -e .

Ici, nous travaillons dans le contexte du SDK, mais sachez que ce même principe utilisant `pip install` est utilisé pour installer un XBlock dans la plateforme Edx.

Vous devriez maintenant avoir un environnement minimal complet. 

Pour rappel, les commandes pour démarrer le serveur :

    source ~/venvs/xblock-sdk/bin/activate
    cd ~/xblock-dev/hellostudent/
    python manage.py runserver 0.0.0.0:8001

Voici ce que vous devriez voir:

![](static/img/indexsdk.png)

![](static/img/hellodk1.png)

## Liens utiles:

La documentation officielle mais en cours de construction.
http://xblock.readthedocs.org/en/latest/

Un tutoriel pour lire et enregistrer des vidéos depuis un xblock.
http://opencraft.com/doc/edx/xblock/tutorial.html

Une liste des xblocks déjà existants.
https://github.com/edx/edx-platform/wiki/List-of-XBlocks


