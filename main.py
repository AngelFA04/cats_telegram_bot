from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
from cats import get_cat

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = os.environ.get('TELEGRAM_TOKEN', '')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot. You can send me /gatitos and I will send you some cute cats")

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f"Hi! Nice to meet you {update.effective_user.first_name} {update.effective_user.last_name}")

start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)

# Function that replies all the messages that are not commands
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Function that capitalize the args received
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


# Function that capitalize the args received
def cats(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_cat())

cats_handler = CommandHandler('gatitos', cats)
dispatcher.add_handler(cats_handler)


# Command to begin the bot
updater.start_polling()