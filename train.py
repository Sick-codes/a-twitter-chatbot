from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatbot import bot
import re
import json
import nltk
trainer =  ChatterBotCorpusTrainer(bot)

trainer1 = ListTrainer(bot)
#a = open('C:\\Users\\cj\\pythonProject1\\chatbot\\ml-chatbot\\TwitterConvCorpus.txt', errors='ignore')
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english")




while True:
   a = input('enter sum shit: ')
   response = bot.get_response(a)
   print(response)
