import telebot
from telebot import types

# t.me/academy_shag_test456bot
API_TOKEN = '1163922176:AAGW3cNqBECqI_tqM1UPrEyWrXvQta__uP8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    # keyboard = types.ReplyKeyboardMarkup(row_width=1)
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Выбери одно из сообщений, я отвечу:', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def reply_text(message):
    if message.text.lower().strip() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель!')
    elif message.text.lower().strip() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!')

'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    keyboard = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Привет')
    itembtn2 = types.KeyboardButton('Пока')
    keyboard.row(itembtn1, itembtn2)
    bot.send_message(message.chat.id, 'Выбери одно из сообщений, я отвечу:', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def reply_text(message):
    if message.text.lower().strip() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель!', reply_markup=types.ReplyKeyboardRemove())
    elif message.text.lower().strip() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!', reply_markup=types.ReplyKeyboardRemove())
'''

bot.polling()