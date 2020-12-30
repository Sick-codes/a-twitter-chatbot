from markovbot import MarkovBot
import os
import time
import requests

def gen_tweet(file):
    tweet_gen = MarkovBot()
    print('reading')
    File = open('4rwchan.txt', 'w',  encoding='cp437', errors='ignore')
    while True:
            tweet_gen.read('4CHAN.txt')
            my_first_text = tweet_gen.generate_text(40, seedword=[u'', u''])
            File.write(my_first_text)
    
def read_from_url(url):
    return requests.get(url).content


gen_tweet('4CHAN.txt')
