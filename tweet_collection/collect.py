import tweet_collection.twitter_connection_setup as connect
import tweepy
import pytest


def get_tweets(lieu, nb_tweets):
    """Prend en argument une chaine de caractère correspondant au lieu et renvoie une 
    liste contenant les textes de chaque tweet contenant le lieu

    Args:
        lieu (chaîne de caractères): Correspond au lieu
        nb_tweets (entier): Nombre de tweets récupérés

    Returns:
        liste: liste de chaine de caractères contenant les textes de chaque tweet récupéré
    """
    try:
        connexion = connect.twitter_setup()  # on se connnecte à l'API twitter
        # on obtient les tweets mentionnant le lieu souhaité
        tweets = connexion.search(
            lieu, lang='en', rpp=100, count=nb_tweets)
        l = []
        for tweet in tweets:
            # on extrait la partie text de tweet, que l'on stocke dans une liste
            l.append(tweet._json['text'])
        return l  # retourne une liste de texte correspondant mentionnant le lieu
    except tweepy.RateLimitError as error:  # si jamais on dépasse le nombre de demande
        print("Nombre maximum de requêtes de Tweets dépassé")
        return []
