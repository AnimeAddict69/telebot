import telebot

API_TOKEN = '799711598:AAEPylDir5KK2oEfgS7wGwe1TIiQ1aW7ivSs'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(
	    message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['about'])
def send_welcome(message):
	bot.reply_to(message, """\
    thisbot is created by rudraksh
""")


bot.polling()
