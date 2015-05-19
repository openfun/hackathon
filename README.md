# Documentation du Hackathon Hac'edX

    http://openfun.github.io/hackathon/

## Génération de la documentation

La documentation peut être générée en local au format pdf :

    git clone https://github.com/openfun/hackathon
    cd hackathon
    sudo apt-get install pandoc texlive texlive-lang-french
    make pdf

Le fichier correspondant peut être téléchargé [ici](https://github.com/openfun/hackathon/raw/regisb/pdfdoc/static/hackathon.pdf).

## Génération du site http://openfun.github.io/hackathon/

Pour publier une version mise à jour du site, il suffit de mettre à jour la branch gh-pages du dépôt github :

    git push origin master:gh-pages

Ou encore :

    make publish
