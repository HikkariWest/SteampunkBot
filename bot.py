import webbrowser
import telebot

API_TOKEN = '1453127728:AAHQb3egcy_UcQpYN5M-VUIB0p-fTPcVoeM'

bot = telebot.TeleBot(API_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'go'])
def send_welcome(message):
    bot.reply_to(message, "hello, site URL")

@bot.message_handler(func=lambda m: True)
def answer(message):
    web = webbrowser.open('http://' + message.text + '.com', new=2)

bot.polling()
