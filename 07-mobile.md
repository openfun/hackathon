---
title: Application mobile OpenedX
layout: default
---

# Les MOOC et usages mobiles

Selon plusieurs sources statistiques (notamment [Gartner](http://www.gartner.com/newsroom/id/2610015)), l'utilisation
des site webs par des outils "mobiles" (tablettes, téléphonne portable) est en train de dépasser celle par les PC traditionnel.

Il est alors évident que créer une application mobile pour suivre son MOOC est devenue nécessaire. Open edX, comme la plupart des
plateformes de MOOC propose une version Mobile de ses applications.

Dans ce document nous allons voir comment installer l'application mobile sous Android et ainsi commencer à pouvoir développer
pour du mobile.

# Les prérequis

## Une IDE pour Android et le SDK

Nous n'allons pas détailler ni conseiller ici d'IDE pour développer sur Android. La documentation essentielle est ici [https://developer.android.com/sdk/index.html](https://developer.android.com/sdk/index.html).
Vous avez principalement le choix entre [Android Studio](https://developer.android.com/tools/studio/index.html) et [Eclipe](https://developer.android.com/tools/help/adt.html).

Les deux ont leur avantages et inconvénients.

La seule chose à retenir ici est que les émulateurs du SDK ne doivent utilise ABI et non pas 'x86', sinon vous ne pourrez
pas avoir un emulateur Android qui coexiste avec la VM de Open edX ([Plus d'info ici](http://stackoverflow.com/questions/16168799/android-emulator-and-virtualbox-cannot-run-at-same-time)).



## L'application Mobile

L'application Mobile OpenedX est disponible ici: https://github.com/edx/edx-app-android
