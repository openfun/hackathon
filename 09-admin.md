---
title: Administrer OpenedX
layout: default
---

# Administration

### MySQL

Vous pouvez acceder au shell MySQL avec l'utilisateur `edxapp001`, le mot de passe est `password` :

    mysql -u edxapp001 -p

Vous pouvez aussi y acceder via Django et la commande `fun` :

    fun lms.dev dbshell


### MongoDB

Quelques commande pour acceder aux collections Mongo :

    mongo
    MongoDB shell version: 2.6.6
    connecting to: test
    > show dbs
    admin                            0.078GB
    cs_comments_service_development  0.078GB
    edxapp                           0.453GB
    local                            0.078GB
    > use edxapp
    switched to db edxapp
    > show collections
    assetstore
    fs.chunks
    fs.files
    modulestore
    system.indexes
    > db.modulestore.find()


### Les logs

Les fichiers de logs propres à edX se trouvent dans `/edx/var/log/`

Les logs applicatifs studio et lms:

    sudo tail -f /edx/var/log/lms/edx.log
    sudo tail -f /edx/var/log/cms/edx.log


Les tracking logs qui aggregent le comportement des utilisateurs du lms :

    /edx/var/log/tracking

## Architecture générale

Comme précisé dans le document suivant [Open edX Architecture](https://open.edx.org/contributing-to-edx/architecture), la plateforme se base notamment sur les technologies suivantes:
- Python
- Django
- Mako Templates
- CoffeeScript
- Backbone.js
- Sass et Bourbon
- Ruby (Forum)

Sur le plan des composants:
- Le LMS
- Le studio
- Les bases de données (MySQL pour les données étudiants et administration, Mongodb pour la structure de cours et données des forums)

Voici un schéma général d'une installation Open edX:
![Edx architecture](https://open.edx.org/sites/default/files/wysiwyg/open-edx-pages/edX_architecture_CMS_LMS_0.png)
