import tweepy
import tweepy.streaming
from dotenv import load_dotenv
import json
import pickle

import os
from clean_data import sick
load_dotenv()
access_key  = os.environ.get('ACESS_TOKEN')
access_secret = os.environ.get('key_secret')
access = os.environ.get('access')
spoop = os.environ.get('soopy')
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(access, spoop)
api = tweepy.API(auth, wait_on_rate_limit=True)


class MyAnalStream(tweepy.StreamListener):
    def on_status(self, status):
        tweet = open('tweets.txt', 'a', encoding='cp437', errors='ignore')
        try:
            print(status.full_text)
            tweet.write(status.full_text)
        except Exception:
            print(status.text)
            tweet.write(status.text)


    def on_error(self, error):
        if error == 420:
            print('smoke weed erra day')
            return False



  
def searchUser username):
     AssholeStream = MyAnalStream()
     shitStream = tweepy.Stream(auth = api.auth, listener=AssholeStream)
     shitStream.filter(track=username, languages=['en'])


    
def searchApi(hashtags, user, file):
     a = open('tweets.txt', 'a', encoding='cp437', errors='ignore')
      for i in api.search([hashtags, user],  languages=['en'], tweet_mode='extended' ):
          a.write('\n' + i.full_text)
          print(i.full_text)





#inst.clean(['https', 'http', 'www', '@'], 'tweets.txt', 'clean_tweets.txt')
#nst.remove_single_chars('tweets.txt', 'clean_tweets.txt')
#inst.remove_special_chars('shit.txt', 'clean_tweets.txt')

