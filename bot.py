#!/usr/bin/env python

from time import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import youtube_music_updater as music_updater
import song_queue as queue

users={}
q=queue.Queue()
def start(update, context):
    update.message.reply_text("Welcome, if you want to add a song to the playing queue, write the title and the author separated by comma")

def help_command(update, context):
    update.message.reply_text("To add a song to the playing queue write <song title>,<author>")

def add(update, context):
    global users
    global q
    if update.message.chat.username in users.keys() and time()-users[update.message.chat.username]<=120:
        update.message.reply_text("Error, you can add a song every 2 minutes")
        return
	
    users[update.message.chat.username]=time()
    if "," in update.message.text.lower():
        update.message.reply_text("Searching and adding the song to the playing queue")
        t=music_updater.MusicUpdater(update.message.text,q)
        t.start()
    else:
        update.message.reply_text("Error, you must send the song title and the author separated by comma")

def main():
    global q
    q.start()
	
    updater = Updater("<Telegram-Bot-Key>", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
	
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, add))

    updater.start_polling()

    updater.idle()
    del q

if __name__ == '__main__':
    main()