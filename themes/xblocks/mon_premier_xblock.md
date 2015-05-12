# Mon premier Xblock 'Hello Student!'

- TODO: Introdction + expliquer où faire tourner ce SDK: pas dans la machine virtuelle à coté de Edx, mais dans l'environement host par exemple.
- TODO: Comment shipper le xblock dans l'appli Edx.
- TODO: Premiers par pour explorer / developer un xblock.

### Installer Python

    sudo apt-get install python

### Installer Pip (le gestionnaire de dépendance python)
 Télécharger ce script python https://bootstrap.pypa.io/get-pip.py
 Puis l'exécuter avec :
 
    sudo python get-pip.py

### Installer le xblock sdk depuis le dépot Github

    sudo apt-get install python-virtualenv
    mkdir -p ~/venvs/
    virtualenv ~/venvs/xblock-sdk
    source ~/venvs/xblock-sdk/bin/activate
    cd ~/
    git clone https://github.com/edx/xblock-sdk.git
    cd ~/xblock-sdk/
    make install
    python manage.py syncdb


### Lancer le serveur de développement

    python manage.py runserver 0:8001

Maintenant depuis votre navigateur allez à cette adresse 127.0.0.1:8001.
Si tout va bien la page suivante devrait apparaître :

![](http://opencraft.com/doc/edx/xblock/_images/workbench_home.png "Optional title")

### Créons la structure de notre xblock avec la commande suivante:

	python script/startnew.py

Le script demande d'abord un nom court pour notre xblock, choisissons 'hellostudent'.
Ensuite rentrons le nom de classe 'HelloStudentXBlock'

Nous avons maitenant un dossier 'hellostudent' contenant la structure du XBlock.

### Afficher 'Hello student'

Ouvrons le fichier *hellostudent/static/html/hellostudent.html* et remplaçons son contenu par :

`<div class="hellostudent_block">
    <p>
        Hello Student !
    </p>
</div>
`

### Enregistrer notre xbock dans le workbench.

Pour afficher notre xblock il est nécessaire de l'installer.
L'installation se fait à travers le fichier setup.py

<pre><code>
	setup(
    name='hellostudent-xblock',
    version='0.1',
    description='Mon premier xblock',
    packages=[
        'hellostudent',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'hellostudent = hellostudent:HelloStudentXBlock',
        ]
    },
    package_data=package_data("hellostudent", ["static", "public"]),
	)
	</code></pre>
	
	cd xblock-sdk/hellostudent
	pip install .

![](https://github.com/openfun/hackathon/blob/jpaille-xblock-doc/themes/static/indexsdk.png?raw=true)

![](https://github.com/openfun/hackathon/blob/jpaille-xblock-doc/themes/static/hellodk1.png?raw=true)
