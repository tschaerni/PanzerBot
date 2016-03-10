import sys
import time
import pprint
import telepot
import re
import random
import logging
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

def leet():
	bot.sendMessage( sys.argv[2], "1337")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    user_id = msg['user']['id']

    zahl = random.randint(1,4)

    if zahl == 1:
        bot.sendMessage(chat_id, "Panzer?")
    elif zahl == 2:
        bot.sendMessage(chat_id, "PANZER!!!!!")
    elif zahl == 3:
        bot.sendMessage(chat_id, "PNAZER!11!!1!!1!!")
    elif zahl == 4:
        bot.sendMessage(chat_id, "BRUMM BRUMM!!!")

    if command == '/source':
        bot.sendMessage(chat_id, "https://github.com/schuwima/PanzerBot/")
    elif command == '@PanzerBot /source':
        bot.sendMessage(chat_id, "https://github.com/schuwima/PanzerBot/")


TOKEN = sys.argv[1]
	
bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print('Listening ...')

sched.add_job(leet, 'cron', hour='13', minute='37')
sched.start()

# Keep the program running.
while 1:
    time.sleep(10)
