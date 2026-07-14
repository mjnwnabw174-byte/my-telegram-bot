import telebot
import requests
from keep_alive import keep_alive

# 1. تعريف التوكن والبوت أولاً
TOKEN = '8877859402:AAESVv6dFFHoSwni-WqcW2jTqNRlCDRYyo8'
WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbywjm4v3ExOL1ynBonQk1hYVzCzoeMUKvPSRTLXoi6cRBYUncUEsNgZ-NZEqPEPMwBu/exec'
bot = telebot.TeleBot(TOKEN)

# 2. تشغيل السيرفر
keep_alive()

# 3. الدوال والأوامر
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🤝 تبادل (تفاعل كامل)", callback_data='exchange'))
    markup.add(telebot.types.InlineKeyboardButton("➕ إضافة حسابي", callback_data='add_account'))
    markup.add(telebot.types.InlineKeyboardButton("🚀 شارك البوت", callback_data='share'))
    markup.add(telebot.types.InlineKeyboardButton("📞 تواصل مع إيطالي", url='https://t.me/mahwb7'))
    markup.add(telebot.types.InlineKeyboardButton("💡 تعليمات العمل", callback_data='help'))
    bot.send_message(message.chat.id, "أهلاً بك يا بطل! (نظام إيطالي المطور)", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'help':
        bot.send_message(call.message.chat.id, "💡 تعليمات: تفاعل بصدق، لا تكن أنانياً، شارك الرابط لترتقي للأعلى!")
    elif call.data == 'add_account':
        msg = bot.send_message(call.message.chat.id, "أرسل رابط حسابك في تيك توك:")
        bot.register_next_step_handler(msg, save_account)

def save_account(message):
    link = message.text
    user = message.from_user.username or "مستخدم"
    requests.get(f"{WEB_APP_URL}?action=addAccount&link={link}&user={user}")
    bot.send_message(message.chat.id, "تم حفظ حسابك!")

bot.polling()
