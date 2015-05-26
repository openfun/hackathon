---
title: Les vidéos
layout: default
---

## Le lecteur vidéo : les bases

Le lecteur vidéo est très utilisé dans les MOOC. On compte en moyenne 30 ou 40 vidéos par MOOC.

Il existe plusieurs lecteurs vidéos disponibles pour Open edX. Le "natif" est celui fourni par la
plateforme qui permet de lire des vidéos de Youtube ([Lecteur Natif dont le manuel est ici](http://edx-partner-course-staff.readthedocs.org/en/latest/creating_content/create_video.html)).

Les autres lecteurs vidéos, notamment celui utilisé par FUN-MOOC, ont des fonctionnalités équivalentes mais en utilisant un hébergement autre que Youtube.

## Caractéristiques d'un lecteur vidéo

La plupart des lecteurs vidéos disponibles peuvent faire les choses suivantes:

1. Intégrer dans Open edX Studio des vidéos par leurs identifiants youtube ou directement par l'URL du fichier vidéo
2. Gérer des sous-titres en plusieurs langues (soit directement par le lecteur soit par l'hébergeur vidéo, cas de FUN-MOOC).
3. Donner à l'utilisateur la possibilité de pause, avance rapide, plein écran, HD ou SD, téléchargement des transcripts (plupart du temps sous-titrage)... (voir Illustration 1)
4. Emmission de "tracking logs" compatibles avec les standards Open edX [Video Interaction Events](http://edx.readthedocs.org/en/latest/internal_data_formats/tracking_logs.html#video-interaction-events)

Illustration 1:

![](http://edx-partner-course-staff.readthedocs.org/en/latest/_images/Video_DownTrans_other.png)

## Faire son lecteur vidéo: les exemples

Ces lecteurs existants peuvent servir de base à une implémentation ou une extension des fonctionalités du lecteur existant.
Le lecteur natif Open edX n'est pas un Xblock et fait encore partie du coeur du code Open edX  [video_module.py](https://github.com/edx/edx-platform/blob/master/common/lib/xmodule/xmodule/video_module/video_module.py), ce qui nécéssite pour modification de faire un "fork", peu désirable.

Voici quelques exemples de lecteurs vidéos intégrés par des Xblocks:

- Un lecteur Video JS: [https://github.com/MarCnu/videojsXBlock](https://github.com/MarCnu/videojsXBlock)
- Le lecteur Paella Player: [https://github.com/polimediaupv/paellaXBlock](https://github.com/polimediaupv/paellaXBlock)
- Le lecteur Ooyala: [https://github.com/edx-solutions/xblock-ooyala](https://github.com/edx-solutions/xblock-ooyala)
- Le lecteur Brightcove: [https://github.com/edx-solutions/xblock-brightcove](https://github.com/edx-solutions/xblock-brightcove)
- Le lecteur DM Cloud:  [Le lecteur DM Cloud](https://github.com/openfun/dmcloud)

## Utilisation des lecteurs natifs

Il est possible d'utiliser les lecteurs natifs des plateforme d'hébergement et de les intégrer dans un Xblock.
Dailymotion, sponsor de cet événement, sera là pour vous guider quant à l'intégration de fonctionnalités proposées dans les projets (Quiz Vidéo...).

Voci quelques liens vers l'API dailymotion.
- Lien vers le site développeur [ https://developer.dailymotion.com/](https://developer.dailymotion.com/)

Il existe un nouveau player HTML5 avec une API similiaire à l'ancienne [API](https://developer.dailymotion.com/documentation#player-api)

Vous trouverez plus d'information ici sur le [Nouveau Lecteur]([http://www.dailymotion.com/player).

### Daily Motion  - Quelques informations supplémentaires

Voici un résumé court des fonctionalités du lecteur, modifiables par l' [API](https://developer.dailymotion.com/documentation#player-api).

Il est possible de :

- modifier les couleurs dans la barre de contrôle
- d'afficher ou non le logo dailymotion dans cette barre
- les partenaires "verified" peuvent appliquer leur logo en bas à droite des videos avec un lien vers leur site.

Le paramètre player qui permet de forcer le nouveau player: GK_PV5=1 dans l'API

Côté accessibilité, le player a été pensé pour répondre aux problématiques: possibilité de naviguer dans le player avec la touche "tab" ; il intègre les fonctionnalités dédiées aux non-voyants ("screen reader" et "voice over") ; les raccourcis clavier de sublime ont été conservés (documentation sur [Sublime](http://docs.sublimevideo.net/keyboard))
