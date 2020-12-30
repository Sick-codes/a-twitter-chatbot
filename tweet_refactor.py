import re
import os
import sqlite3
import time
from chatbot import bot
from clean_data import sick
import tweepy.streaming
from markovbot import MarkovBot
from dotenv import load_dotenv


load_dotenv()
access_key = os.environ.get('ACESS_TOKEN')
access_secret = os.environ.get('key_secret')
access = os.environ.get('access')
spoop = os.environ.get('soopy')
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(access, spoop)
api = tweepy.API(auth, wait_on_rate_limit=True)


conn = sqlite3.connect('tweets.db', check_same_thread=False)
c = conn.cursor()
demBot = MarkovBot()







class Utils(object):
    @classmethod
    def bot_response(self, text):
        return bot.get_response(sick.clean_text(
                ['@', 'http', '#'], text))


    @classmethod
    def gen_text(self, file='', amount=1):
        inst = MarkovBot()
        inst.read(file)
      #  while True:
        sick = []
        for i in range(amount):
           text = inst.generate_text(25, seedword=[''])
           sick.append(text)
        return sick





class db(Utils):
    @classmethod
    def check_id(cls, id_):
        c.execute('SELECT * FROM tweets WHERE id=? ', (id_,))
        print(str(id_) in str(c.fetchall()))



    def getData(self):
        c.execute('SELECT * FROM tweets')
        return c.fetchall()


    def create_table(self):
        c.execute('CREATE TABLE tweets(id INT)')



    @classmethod
    def insert_data(cls, id_):
        if db.check_id(id_):print('sorry it already exists')
        else:
            c.execute('INSERT INTO tweets values(?)', (id_,))
            conn.commit()
            print('yay')


    @classmethod
    def remove_duplicates(cls, id_):
        c.execute('SELECT * FROM tweets WHERE id=?',
                     (id_,))
        if len(c.fetchall()) > 1:
            c.execute('DELETE FROM tweets WHERE id=?', (id_,))
            c.execute('INSERT INTO tweets WHERE id=?', (id_,))
            conn.commit()
        else:return 'e'




class SickStream(tweepy.StreamListener):
    def on_status(self, status):
        try:
            print(status.text, status.id)
            db.insert_data(status.id)
        except Exception:print('ad')


    def on_error(self, code):
        if code == 420:
            print('smoke weed everyday')
            return False




class Search(object):
    def keywords(self,  search_word):
        for i in api.search(search_word, tweet_mode='extended'):
            db.insert_data(i.id)
            print(i.full_text)


    def Stream(self,  searchWord):
        sickInstance = SickStream()
        stream = tweepy.Stream(auth=api.auth, listener=sickInstance)
        stream.filter(track=searchWord, languages=['en'])


    def get_replies(self, user_id):
        gang = api.search(q=f'to:{user_id}',
                result_type='all')
        for i in gang:
            db.insert_data(i.id)
            print(i.id)



    def user(self, user_name):
        gang = api.user_timeline(user_name)
        for tweet_text in gang:
            db.insert_data(tweet_text.id)
            print(tweet_text.text)


    def UpdateStatus(self, text):
        api.update_status(text)



class reply(Search):
    @classmethod
    def database(cls, amount):
        c.execute('SELECT * FROM tweets')
        for i in range(amount):
            pass



    @classmethod
    def to_status(cls, tweet_id):
        try:
            text = api.get_status(tweet_id)
            print(text.text)
            gang = Utils.bot_response(text.text)
            api.update_status(gang, in_reply_to_status_id=text.id)
            print(gang)
        except Exception as e:print(e)
 

    @classmethod
    def tag(cls):
        for i in api.search('#ask_ml', tweet_mode='extended'):
            db.insert_data(i.id)
            resp = Utils.bot_response(i.full_text)
            print(i.id)
            if db.check_id(i.id) == True:
                print('so sorry')
            else:
                resp = Utils.bot_response(i.full_text)
                api.update_status(f'@{i.user.screen_name} {resp}')


search = Search()
inst2 = reply()
instance = Utils()
database = db()
