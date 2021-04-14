#This file controls the chat bot's Twitter features
#It will return the chat bot's recent tweets, number of followers, and number of following
import sys      #System tool needed for authenticating
import tweepy   #API for Twitter

class twitter:

    def __init__(self,inp):
        #takes in input of user
        self.inp = inp
    
    def twitter_auth(self):
        try:
            consumer_key = '6ILEz0rWBW3E1UxgV8x1xLZsj'
            consumer_secret = 'O18GikmIrybwmaCndxMpwKD6ghS3NJwQC0owlapOjpk0oeq773'
            access_token = '835735789191323649-sk795I9VpK2Nrbwgs3ZZ1mn0kKtD7nd'
            access_secret = 'USMWxS5lQOiqhqSdC8GUS4Oe39r23A2c7mbB0DENP3n96'
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)   #authorizes Twitter authentication keys
            auth.set_access_token(access_token, access_secret)
        except KeyError:
            sys.stderr.write("TWITTER_* environment variable not set\n")    #authorization was unsuccessful
            sys.exit(1) #quit program
        return auth

    def get_twitter_client(self):
        auth = self.twitter_auth()  #sets authorization of twitter API
        client = tweepy.API(auth)   #API client is activated through tweepy and can be used in program
        return client

    def retrieve_tweets(self):
        user = 'justintrudeau'  #username of Justin Trudeau's Twitter
        client = self.get_twitter_client()
        for status in tweepy.Cursor(client.user_timeline, screen_name=user).items(1):   #retrieves Justin Trudeau's most recent tweet data
            return status.text  #returns text in Justin Trudeau's recent tweet

