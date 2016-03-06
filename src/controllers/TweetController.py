import json
import os
import tweepy
from src import Main
from src.services import Listener


class TweetController(object):
    """docstring for Controller"""

    def __init__(self, server):
        self.auth = tweepy.OAuthHandler(Main.config["consumer_key"], Main.config["consumer_secret"])
        self.auth.set_access_token(Main.config["access_token"], Main.config["access_token_secret"])
        self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())

        def fetchTweets(self):
            pub_tweets = self.api.home_timeline()
            f = open(os.path.dirname(__file__) + "../../Data/tweets.json", "w")
            f.write(json.dumps(pub_tweets))

        def startStreamingTweets(self, keywords):
            self.tweet_listener = Listener()
            self.stream = tweepy.Stream(auth=self.auth, listener=self.tweet_listener)
            self.stream.filter(track=keywords, async=True)

        def listOfTweets(self):
            f = open(os.path.dirname(__file__) + "../../Data/tweets.json")
            return f.read()

        def stopStreamingTweets(self):
            self.stream.disconnect()
