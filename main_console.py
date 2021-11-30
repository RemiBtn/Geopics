from tweet_collection.collect import get_tweets
from tweet_analysis.key_words import get_key_words, reduction_dico
from pics_extraction.get_infos_images import get_dict, extract_url_dict
from display.display_images import afficher


def demo(nb_pics_par_keyword, nb_tweets):
    """Lance la démo. Prend en argument une liste contenant le nombre de photos associées à chaque mot clef

    Args:
        nb_pics_par_keyword (liste): liste d'entiers, représentant le nombre de photos associées à chaque mot clef
        nb_tweets (entier): nombre de tweets qu'on récupère
    """

    lieu = input('Choisissez le lieu :\n').capitalize()
    # liste contenant les textes des tweets mentionnant le lieu
    tweets = get_tweets(lieu, nb_tweets)
    # on récupère les mots clés à partir de cette liste
    nb_keyword = len(nb_pics_par_keyword)*3
    keywords = reduction_dico(tweets, nb_keyword)
    # on extrait les URL des images associées aux mots clés
    url, compteur = [], 0
    # pour chaque mot clef, on cherche les urls des images associées
    for keyword in keywords:
        new_urls = extract_url_dict(keyword, nb_pics_par_keyword[compteur])
        # le système de compteur permet d'aller chercher des mots clés supplémentaire (les suivants dans la liste) si les premiers n'obtiennent pas d'image
        if new_urls and compteur < len(nb_pics_par_keyword):
            url.extend(new_urls)
            compteur += 1
        if compteur == len(nb_pics_par_keyword):
            break
    afficher(url)


demo([6, 4, 3, 3], 20)
