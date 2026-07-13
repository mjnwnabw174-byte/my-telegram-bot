import telebot
from keep_alive import keep_alive
TOKEN = "8634311118:AAF9ZRQCW5y55AggjL65s52nvo2Gzj1EWAk"
bot = telebot.TeleBot(TOKEN)
keep_alive()
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت يعمل 24/7! نظام التبادل مفعل.")
bot.polling()

