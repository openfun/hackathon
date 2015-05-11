# Hack'edX

## Présentation

Edx est une platforme web qui permet de délivrer des cours en ligne ouverts à tous, les MOOCs - Massive Online Open Courses.

Les cours sont édités dans le « Studio ». Le Studio est une section réservée aux enseignants et aux personnes responsables de maintenir les cours. Il s'agit d'une interface web d'où l'on peut éditer les contenus de cours, gérer les vidéos et les autres ressources à destination des apprenants. Depuis le Studio, on peut gérer les calendriers de cours, gérer les barêmes de notation des apprenants, concevoir les quiz, etc.

Le LMS - Learning Management System, est la section publique de la plateforme Edx. Les cours qui sont édités dans le Studio sont publiés dans le LMS et disponibles aux apprenants. Le LMS est la partie la plus exposée et permet notamment aux apprenants de se connecter et de suivre leur cours.
Il s'agit de https://www.france-universite-numerique-mooc.fr par exemple..
Les apprenants peuvent s'inscrirent, consulter les cours, répondre aux quiz, accéder aux résultats, etc.

Lorsque vous installez OpenFUN ou Open edX, vous aurez sur une même machine les deux "sites". L'un répondant sur http://127.0.0.1:8000 (LMS) et l'autre sur http://127.0.0.1:8001 (Studio)



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

    # De même, dans un autre terminal, vous pouvez lancer le Studio/CMS :
    fun cms.dev --fast

Le Studio/CMS est alors visible à l'adresse http://127.0.0.1:8001.

Vous pouvez également lancer les tests associés à FUN :

    # Notez que les settings de test sont différents de ceux de dev
    fun lms.test ../fun-apps/

Sous le capot, 'fun' est un raccourci permettant d'exécuter une variété de
commandes. Pour plus d'informations, consultez la documentation de fun-cmd :
https://github.com/openfun/fun-cmd
