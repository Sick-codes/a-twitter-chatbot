import tweepy
import tweepy.streaming
from  tweet_refactor import insert_data
import json
import os


auth = tweepy.OAuthHandler()
auth.set_access_token()
api = tweepy.API(auth, wait_on_rate_limit=True)

class MyAnalStream(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        insert_data(status.id)
        

    
    def on_error(self, error):
        if error == 420:
            print('smoke weed erra day')
            return False


def searchUser(username):
    AssholeStream = MyAnalStream()
    shitStream = tweepy.Stream(auth=api.auth, listener=AssholeStream)
    shitStream.filter(track=username, languages=['en'])


def searchApi(hashtags,  file):
    a = open('tweets.txt', 'a', encoding='cp437', errors='ignore')
    for i in api.search([hashtags], languages=['en'], tweet_mode='extended'):
        a.write('\n' + i.full_text)
        print(i.full_text)


searchUser('olive garden')
