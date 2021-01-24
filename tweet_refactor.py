import os
from clean_data import clean_text
import sqlite3
from chatbot import bot
import tweepy.streaming
from markovbot import MarkovBot
from dotenv import load_dotenv
import time

auth = tweepy.OAuthHandler(')
auth.set_access_token(')
api = tweepy.API(auth, wait_on_rate_limit=True)
conn = sqlite3.connect('tweets.db', check_same_thread=False)
c = conn.cursor()
demBot = MarkovBot()


def create_table():
    c.execute('CREATE TABLE tweets(id INT)')


def delete_data(data):
    c.execute('DELETE FROM tweets WHERE id=?', (data,))
    conn.commit()


def bot_response(text):
    return bot.get_response(clean_text(
        ['@', 'http', '#'], text))


def gen_text(file='', amount=1):
    inst = MarkovBot()
    inst.read(file)
    #  while True:
    return [inst.generate_text(seed=[], 25) for i in range(amount)]


def check_id(id_):
    c.execute('SELECT * FROM tweets WHERE id=? ', (id_,))
    return str(id_) in str(c.fetchall())


def insert_data(id_):
    if check_id(id_):
        print('sorry it already exists')
    else:
        c.execute('INSERT INTO tweets values(?)', (id_,))
        conn.commit()
        print('yay')


def remove_duplicates(id_):
    c.execute('SELECT * FROM tweets WHERE id=?', (id_,))
    if len(c.fetchall()) > 1:
        c.execute('DELETE FROM tweets WHERE id=?', (id_,))
        c.execute('INSERT INTO tweets WHERE id=?', (id_,))
        conn.commit()
    else:
        return 'e'


class SickStream(tweepy.StreamListener):
    def on_status(self, status):
        x = bot_response(status.text)
        time.sleep(30)
        api.update_status(f'@{status.user.screen_name}', x)
        print(x)

    def on_error(self, code):
        if code == 420:
            print('smoke weed everyday')
            return False


def keywords(search_word):
    for i in api.search(search_word, tweet_mode='extended'):
        insert_data(i.id)
        print(i.full_text)


def tweet_stream(search_word):
    sick_instance = SickStream()
    stream = tweepy.Stream(auth=api.auth, listener=sick_instance)
    stream.filter(track=search_word, languages=['en'])


def get_replies(user_id):
    gang = api.search(q=f'to:{user_id}',
                      result_type='new')
    for i in gang:
        insert_data(i.id)
        print(i.id)


def user(user_name):
    gang = api.user_timeline(user_name)
    for tweet_text in gang:
        insert_data(tweet_text.id)
        print(tweet_text.text)


def tweet(text):
    api.update_status(text)


def keywords_database(keyword, amount):
    c.execute('SELECT * FROM tweets')
    for i, l in enumerate(c.fetchall()):
       # print(i)
        tweets = api.get_status(1345014550404374534)
        print(tweets.text)
        #if keyword in tweets.text:
         #   print('ae')
#

def to_status(tweet_id):
    text = api.get_status(tweet_id, tweet_mode='extended')
    gang = bot_response(text.full_text)
    api.update_status(gang, in_reply_to_status_id=text.id)
    print(gang)


def tag():
    for i in api.search('#ask_ml', tweet_mode='extended'):
        insert_data(i.id)
        if check_id(i.id):
            print('so sorry')
        else:
            resp = bot_response(i.full_text)
            api.update_status(f'@{i.user.screen_name}', resp)


keywords_database('hello', 1)
