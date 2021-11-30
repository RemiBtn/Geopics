# Projet GeoPics du Groupe 2 Pôle Portwiture Coding Weeks - Semaine 2

## User story

En tant que touriste lassé des mauvaises surprises (cf syndrôme de Paris), l'utilisateur souhaite une représentation plus réaliste et visuelle de son futur lieu de villégiature. 

## Finalité du programme  

GeoPics permet en entrant un lieu d'obtenir une mosaïque d'images le décrivant. Ces images sont obtenues en analysant les tweets récents mentionnant la destination de l'utilisateur.

## Dépendances

Les modules requis et les versions associées sont listés dans le fichier ``requirements.txt``.

Pour les installer facilement, il suffit d'entrer la commande suivante dans le terminal :

    pip install -r requirements.txt

## Prérequis pour le bon fonctionnement des programmes

Nous avons mis en ligne deux templates nommés ``credentials_template_twitter.py`` et ``credentials_flickr.py``, respectivement situés dans les dossiers ``tweet_collection`` et ``pics_extraction`` . Pour utiliser les programmes, il faut au préalable compléter à l'aide de vos codes développeur Twitter et Flickr les champs indiqués en commentaires. Une fois ceci fait, il vous faut renommer ``credentials_template_twitter.py`` en ``credentials.py`` et ``credentials_template_flickr.py`` en ``credentials_flickr.py`` .


## Version "Démo"

Pour un usage en version "démo" avec les fonctionnalités principales, se placer dans le dossier geopics et exécuter le fichier ``main_interface_graphique.py`` en tapant la commande suivante dans le terminal :

    python -m main_interface_graphique

La version originelle (le MVP sans interface graphique) peut également être lancée avec la commande :

    python -m main_console

## Exécution d'un autre programme 

Pour exécuter un programme autre que ``main_console.py`` ou ``main_interface_graphique.py``, par exemple ``nom_programme.py`` dans le répertoire ``nom_dossier``, entrer la commande suivante dans le terminal :

    python -m nom_dossier.nom_programme

## Fonctionnalités disponibles

- collecte de tweets mentionnant un lieu entré par l'utilisateur via ``tweet_collection/collect.py``.

- extraction des adjectifs présents dans un texte en anglais et collecte de mots-clés sous forme d'un dictionnaire de type 

``{['mot-clé'] : nombre_d_apparitions}`` via ``tweet_analysis/key_words.py``.

- affichage d'une image à partir de son adresse url via ``pics_extraction/flickr_extraction.py``.

- collecte d'informations d'images provenant de Flickr sous forme d'une liste contenant un dictionnaire associé à chaque image via ``pics_extraction/get_infos_images.py``.

- affichage d'une mosaïque de 16 images à partir des adresses url de ces images via ``display/display_images.py``.

- redimensionnement d'une image via ``display/reshape_image.py``.

## Présentation des membres du Groupe 2 GeoPics du Pôle Portwiture

Daniel Gong : étudiant à CentraleSupélec motivé

Saber Taieb : étudiant en première année à CentraleSupélec 

Rémi Boutonnier : étudiant à CentraleSupélec qui aime le sport

Alexandre Michel : sympathique étudiant de CS

Pierre Jaumain : débutant en informatique en 1A à CS
