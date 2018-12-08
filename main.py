#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import datetime
from modules import storage

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)
flag = False

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	global flag
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hi! Please send the link of Repl.it Project (only the link)')
	flag = True


def help(bot, update):
	global flage
	"""Send a message when the command /help is issued."""
	update.message.reply_text('The url of the Repl.it project have to be like this: https://repl.it/@Utente/ProjectName\nThe answer must include only the link\n\nCommand list:\n/start -> Starts the conversation\n/help -> Give help\n/update -> Updates the answer')
	flag = False


def echo(bot, update):
	"""Echo the user message."""
	global flag
	if flag == True:
		# answer received
		link = update.message.text
		from_user = update.message.from_user['username']
		date = (datetime.datetime.now()+ datetime.timedelta(hours=1)).strftime("%y-%m-%d-%H-%M")

		update.message.reply_text("date: " + date+ "\nfrom_user: " + str(from_user) + "\nrisposta: " +link)
		flag = False
	else:
		update.message.reply_text("Non inviare più volte la risposta!\nPer aggiornare la risposta usa il comando /update {link}")


def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)


def main():
	"""Start the bot."""
	# Create the EventHandler and pass it your bot's token.
	updater = Updater("643749538:AAHlNULp8uSed4_gWOJSh-DokuJyB-La5V0")

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))

	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	print("server is running!")
	main()
	
