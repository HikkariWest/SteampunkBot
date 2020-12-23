import webbrowser
import telebot

TOKEN = "1453127728:AAHQb3egcy_UcQpYN5M-VUIB0p-fTPcVoeM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def send_welcome(message):
	bot.reply_to(message, "Hello, site URL")

@bot.message_handler(func=lambda m: True)
def answer(message):
	web = webbrowser.open('https://' + message.text + '.com', new=2)

bot.polling()
