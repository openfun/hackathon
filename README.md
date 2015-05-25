# Documentation du Hackathon #OpenedXHack

[http://openfun.github.io/hackathon/](http://openfun.github.io/hackathon/)

## Génération de la documentation

La documentation peut être générée en local au format pdf :

    git clone https://github.com/openfun/hackathon
    cd hackathon
    sudo apt-get install pandoc texlive texlive-lang-french
    make pdf

Le fichier correspondant peut être téléchargé [ici](https://github.com/openfun/hackathon/raw/master/static/hackathon.pdf).

## Génération des pages Github

Pour publier une version mise à jour du site, il suffit de mettre à jour la branch gh-pages du dépôt github :

    git push origin master:gh-pages

Ou encore :

    make publish

En réalité, il suffit de mettre à jour la branche master et
[Jenkins](http://ci.alt.openfun.fr/job/hackathon-github-pages/) se chargera de
mettre à jour le site github.
