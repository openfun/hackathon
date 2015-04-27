# Hack'edX

## Présentation

EDX est une plate-forme de MOOC (Massive open online courses).
Ce sont des cours en ligne ouverts à tous. Les MOOCS permettent un accès facile à un ensemble de formations (histoire, maths, physique, droit économie...)

snap

Les moocs ne sont pas composés uniquement de vidéos de cours. Ils s'accompagnent aussi de nombreuses activités, jeux

snap.

Les étudiants suivent les mooc depuis le LMS:

snap

Et les professeurs concoivent les mooc depuis un (CMS content management system), appelé aussi Studio:

snap


## Premiers pas

### Installation d'une machine virtuelle OpenFUN

Les composants nécessaires à l'installation de FUN ou d'edX sont nombreux et relativement complexes ; c'est pourquoi il existe des machines virtuelles (VM) disponibles en simple téléchargement qui permettent de commencer rapidement à tester ces applications. Dans la suite de cette section, nous allons voir les étapes à suivre pour obtenir un environnement de développement fonctionnel.

### Téléchargement

Les VM OpenFUN sont disponibles au téléchargement via bittorrent. Si vous ne
disposez pas d'un client bittorrent (tel que Transmission, Azure ou Deluge),
vous devrez télécharger les VM en HTTP, ce qui risque d'être plus lent et de
saturer les serveurs de FUN.

Les fichiers .torrent correspondant aux différentes version d'OpenFUN sont
disponibles ici : http://files.alt.openfun.fr/vagrant-images/fun/

Vous pouvez télécharger le fichier openfun-\*.torrent correspondant à la
version la plus récente d'OpenFUN dans votre client bittorrent favori.

### Lancement de la machine virtuelle

Une fois que l'image d'OpenFUN est téléchargée, vous pouvez procéder à son
lancement. Pour cela, clonez le dépôt fun-boxes et consultez le README :

    git clone https://github.com/openfun/fun-boxes
    cd fun-boxes
    cat README.rst

Suivez les instructions pour l'installation des dépendances et le lancement de
la release que vous avez téléchargée. Vous devrez notamment définir les
variables d'environnement suivantes :

    export VAGRANT_BOXES=/chemin/vers/mon/repertoire/de/torrents/
    export FUN_RELEASE=2.11 # Si vous avez téléchargé la version 2.11 d'OpenFUN

### Lancement d'un serveur web

Si vous avez correctement lancé votre machine virtuelle, vous pouvez maintenant vous y connecter via ssh et lancer un serveur web local :


    ######### Commande exécutée sur votre machine hôte
    vagrant ssh

    ######### Commandes exécutées dans la VM

    # La plupart des applications sont exécutées par l'utilisateur edxapp
    sudo su edxapp 

    # Cette commande réalise à la fois l'installation des dépendances, la
    # collecte des données statiques et le lancement de l'application LMS
    fun lms.dev

Ouvrez maintenant votre navigateur (de votre machine hôte) à l'adresse
http://127.0.0.1:8000 : vous devriez voir apparaître la page d'accueil de FUN.
Win!

    # Pour sauter les phases de vérification de l'environnement, vous pouvez
    # exécuter à la place de la commande précédente :
    fun lms.dev --fast

    # De même, dans un autre terminal, vous pouvez lancer le CMS :
    fun cms.dev --fast

Le CMS est alors visible à l'adresse http://127.0.0.1:8001.

Vous pouvez également lancer les tests associés à FUN :

    # Notez que les settings de test sont différents de ceux de dev
    fun lms.test ../fun-apps/

Sous le capot, 'fun' est un raccourci permettant d'exécuter une variété de
commandes. Pour plus d'informations, consultez la documentation de fun-cmd :
https://github.com/openfun/fun-cmd
