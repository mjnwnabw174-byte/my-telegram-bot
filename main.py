import telebot
from keep_alive import keep_alive
TOKEN = "8877859402:AAESVv6dFFHoSwni-WqcW2jTqNRlCDRYyo8"
bot = telebot.TeleBot(TOKEN)
keep_alive()
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت يعمل 24/7! نظام التبادل مفعل.")
bot.polling()

