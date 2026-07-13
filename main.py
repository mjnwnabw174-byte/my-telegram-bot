import telebot
from keep_alive import keep_alive
TOKEN = "8643869272:AAEOYScqMRKaqKq8oUNS25mWP7TrJ9k7Mk4"
bot = telebot.TeleBot(TOKEN)
keep_alive()
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت يعمل 24/7! نظام التبادل مفعل.")
bot.polling()

