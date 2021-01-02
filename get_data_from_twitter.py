import tweepy
import tweepy.streaming
from  tweet_refactor import insert_data
import json
import os


auth = tweepy.OAuthHandler('h4U32ZuULZzCXWSxbW056ah1y','5XGi2f9gVtqRAfPioQvwYxuNdQFxpT7lX3WXPZoo9a2WXDeDpb')
auth.set_access_token('1323402718124347393-xXlIChPtqWC6jad2laZI91uW1yN5MR', 'NoDUxrtgC57VjQIGOxlTkKHzgW9yGFz9MkGSAIe3f7iZg')
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