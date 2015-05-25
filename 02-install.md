---
title: Installation d'une machine virtuelle OpenFUN / edX
layout: default
---

# Installation d'une machine virtuelle OpenFUN / edX {#install}

Les composants nécessaires à l'installation de FUN ou d'edX sont nombreux et
relativement complexes ; c'est pourquoi il existe des machines virtuelles (VM)
disponibles en simple téléchargement qui permettent de commencer rapidement à
tester ces applications. Dans la suite de cette section, nous allons voir les
étapes à suivre pour obtenir un environnement de développement fonctionnel.

### Téléchargement (optionnel mais fortement recommandé)

Les VM OpenFUN sont disponibles au téléchargement via bittorrent. Si vous ne
disposez pas d'un client bittorrent (tel que
[Transmission](http://www.transmissionbt.com/), [Vuze](http://www.vuze.com/) ou
[Deluge](http://deluge-torrent.org/)),
vous devrez télécharger les VM en HTTP, ce qui risque d'être plus lent et de
saturer les serveurs de FUN.

Les fichiers .torrent correspondant aux différentes version d'OpenFUN sont
disponibles ici : [http://files.alt.openfun.fr/vagrant-images/fun/](http://files.alt.openfun.fr/vagrant-images/fun/)

Vous pouvez télécharger le fichier openfun-\*.torrent correspondant à la
version la plus récente d'OpenFUN dans votre client bittorrent favori.

Avant de créer votre VM, il faudra indiquer à Vagrant le répertoire dans lequel vous avez téléchargé les images :


    export VAGRANT_BOXES=/chemin/vers/mon/repertoire/de/torrents/
    export FUN_RELEASE=2.11 # Si vous avez téléchargé la version 2.11 d'OpenFUN

### Clonage des dépôts de code Open edx et OpenFUN (optionnel mais recommandé aux développeurs)

Cette étape optionnelle est néanmoins bien pratique si vous comptez contribuer
au code d'Open edX ou de FUN. En effet, vous voudrez vraisemblablement éditer
le code source dans votre machine hôte avec votre IDE favori avant de voir le
résultat dans votre VM. Pour cela :

    # Choisissez un répertoire dans lequel cloner les dépôts de code nécessaires
    mkdir /home/user/repos
    cd /home/user/repos/

    # Clonez les dépôts
    git clone https://github.com/openfun/fun-apps
    git clone https://github.com/openfun/edx-platform # cela peut prendre un peu de temps...
    mkdir themes && git clone https://github.com/openfun/edx-theme themes/fun/

    # Indiquez à Vagrant le répertoire dans lequel vous avez cloné les dépôts
    export VAGRANT_MOUNT_BASE=/home/user/repos

### Lancement de la machine virtuelle


Après avoir (éventuellement) réalisé les étapes ci-dessus, vous êtes prêt à
lancer votre machine virtuelle.  Pour cela, clonez le dépôt fun-boxes :

    git clone https://github.com/openfun/fun-boxes
    # le readme est plein d'instructions fort utiles
    cat fun-boxes/README.rst

Lancez votre machine virtuelle :

    cd fun-boxes/releases/
    vagrant up

En cas de problème, pensez à consulter le README dans lequel votre problème est
peut-être déjà décrit.

### Lancement d'un serveur web

Si vous avez correctement lancé votre machine virtuelle, vous pouvez maintenant
vous y connecter via ssh et lancer un serveur web local :


    ######### Commande exécutée sur votre machine hôte
    vagrant ssh

    ######### Commandes exécutées dans la VM

    # La plupart des applications sont exécutées par l'utilisateur edxapp
    sudo su edxapp

    # Cette commande réalise à la fois l'installation des dépendances, la
    # collecte des données statiques et le lancement de l'application LMS
    fun lms.dev run

Ouvrez maintenant votre navigateur (de votre machine hôte) à l'adresse
[http://127.0.0.1:8000](http://127.0.0.1:8000) : vous devriez voir apparaître la page d'accueil de FUN.
Win!

    # Pour sauter les phases de vérification de l'environnement, vous pouvez
    # exécuter à la place de la commande précédente :
    fun lms.dev run --fast

    # De même, dans un autre terminal, vous pouvez lancer le Studio/CMS :
    fun cms.dev run --fast

Le Studio/CMS est alors visible à l'adresse http://127.0.0.1:8001.

Vous pouvez également lancer les tests associés à FUN :

    # Notez que les settings de test sont différents de ceux de dev
    fun lms.test test ../fun-apps/
    fun cms.test test ../fun-apps/

Sous le capot, 'fun' est un raccourci permettant d'exécuter une variété de
commandes. Pour plus d'informations, consultez la documentation de fun-cmd :
[https://github.com/openfun/fun-cmd](https://github.com/openfun/fun-cmd)


### Le forum

Le forum fonctionne avec un service REST Ruby qui utilise Mongo pour stocker les messages, ElasticSearch pour les indexer et un client Django qui se trouve dans le dépôt `edx-platform`.

Pour lancer le service forum dans un terminal :

    sudo su forum
    ruby app.rb -p 18080
