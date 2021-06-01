import telebot

# t.me/academy_shag_test456bot
API_TOKEN = '1163922176:AAGW3cNqBECqI_tqM1UPrEyWrXvQta__uP8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!')

# bot.reply_to(message, 'Привет, мой создатель!')
'''
@bot.message_handler(content_types=['text'])
def reply_text(message):
    if message.text.lower().strip() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель!')
    elif message.text.lower().strip() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!')
'''

'''
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower().strip() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель!')
    elif message.text.lower().strip() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!')
    elif message.text.lower().strip() == 'покажи зил':
        zil_photo = open(r'E:\Фото\iPad\ЗИЛ 41041 (Білий)\2156160.jpg', 'rb')
        bot.send_photo(message.chat.id, zil_photo)
        bot.send_message(message.chat.id, 'Ещё показать?')
    elif message.text.lower().strip() == 'да':
        zil_photo2 = open(r'E:\Фото\iPad\ЗИЛ 41041 (Білий)\2125757.jpg', 'rb')
        bot.send_photo(message.chat.id, zil_photo2)
'''

bot.polling()