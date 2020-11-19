from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('1419291546:AAHs74alHPAj3m1Y1GA7uGrIpZ4M5BZmTAc')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()