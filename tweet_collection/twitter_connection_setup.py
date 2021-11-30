import tweepy
from tweet_collection.credentials import *  # We import our access keys


def twitter_setup():
    """    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py

    Returns:
        The authentified API 
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api
