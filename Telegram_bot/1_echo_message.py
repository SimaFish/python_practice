import telebot

# t.me/academy_shag_test456bot
API_TOKEN = '1163922176:AAGW3cNqBECqI_tqM1UPrEyWrXvQta__uP8'
bot = telebot.TeleBot(API_TOKEN)

# A function which is decorated by a message handler can have an arbitrary name,
# however, it must have only one parameter (the message).
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

# Named greeting message
'''
@bot.message_handler(commands=['start'])
def start_message(message):
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, 'Привет, {0}, давай общаться!'.format(first_name))
'''

bot.polling()