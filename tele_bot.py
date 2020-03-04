import os
import random
import telepot

TOKEN= "778276850:AAFazgnlyG2m_Th_pT39Fa5aCIZ8-lu2tBE" #This is the key given when making a new telegram Bot

#emojis
#joker_emoji=u'\U+1F921' # the clown emoji just for fun


def loop(msg): # this is just so it keeps looping
    chat_id = msg['chat']['id']
    message = msg['text']

bot=telepot.Bot(TOKEN)
bot=message_loop(loop)

def files(): #not working right now
    file=random.choice(open(f'{message}.txt','rt').readlines())
    bot.sendMessage(file)

if message == Joker:
    bot.sendMessage("why so serious")
