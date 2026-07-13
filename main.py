import telebot
import requests

# التوكن الخاص ببوتك
TOKEN = '8877859402:AAESVv6dFFHoSwni-WqcW2jTqNRlCDRYyo8' 

# رابط الـ Web App الخاص بك
WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbywjm4v3ExOL1ynBonQk1hYVzCzoeMUKvPSRTLXoi6cRBYUncUEsNgZ-NZEqPEPMwBu/exec' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("تبادل التفاعل", callback_data='exchange'))
    markup.add(telebot.types.InlineKeyboardButton("إضافة حسابي", callback_data='add_account'))
    markup.add(telebot.types.InlineKeyboardButton("تواصل مع المطور", callback_data='contact'))
    bot.send_message(message.chat.id, "أهلاً بك يا بطل في نظام التبادل المباشر!\nاختر ما تريد:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'add_account':
        msg = bot.send_message(call.message.chat.id, "أرسل رابط حسابك في تيك توك الآن:")
        bot.register_next_step_handler(msg, save_account)
    elif call.data == 'exchange':
        bot.send_message(call.message.chat.id, "جاري جلب الحسابات من الدور... انتظر قليلاً.")
    elif call.data == 'contact':
        bot.send_message(call.message.chat.id, "للتواصل مع المطور: @YourUsername") # ضع يوزرك هنا

def save_account(message):
    link = message.text
    user = message.from_user.username or "مستخدم"
    try:
        # إرسال البيانات لـ Google Sheet
        response = requests.get(f"{WEB_APP_URL}?action=addAccount&link={link}&user={user}")
        if response.status_code == 200:
            bot.send_message(message.chat.id, "تم حفظ حسابك بنجاح! أنت الآن في الدور.")
        else:
            bot.send_message(message.chat.id, "حدث خطأ أثناء الاتصال بالجدول.")
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ: {str(e)}")

bot.polling()
