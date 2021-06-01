import telebot
from telebot import types

# t.me/academy_shag_test456bot
API_TOKEN = '1163922176:AAGW3cNqBECqI_tqM1UPrEyWrXvQta__uP8'
bot = telebot.TeleBot(API_TOKEN)

dict_chat = {}

key = {
    1:"Вопрос 1",
    2:"Вопрос 2",
    3:"Вопрос 3"
}

question = {
    1:"Какого цвета учебник?",
    2:"Как называется предмет?",
    3:"Как меня зовут?"
}

reply = {
    1:"красный",
    2:"математика",
    3:"николай"
}

def coalesce(*args):
    return next((i for i in args if i is not None), None)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, {0}!'.format(message.from_user.first_name))
    bot.send_message(message.chat.id, 'Чтобы начать игру введи /game')

@bot.message_handler(commands=['game'])
def game_start(message, reply_text=None):
    keyboard = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text=key[1], callback_data=1)
    call2 = types.InlineKeyboardButton(text=key[2], callback_data=2)
    call3 = types.InlineKeyboardButton(text=key[3], callback_data=3)
    keyboard.row(call1, call2, call3)
    bot.send_message(message.chat.id, coalesce(reply_text, 'Начнём игру'), reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: call.data=='1')
def call_back_request(call):
    n = int(call.data)
    answer = bot.send_message(call.message.chat.id, question[n])
    bot.register_next_step_handler(answer, go_answer1)

def go_answer1(answer):
    if answer.text.lower() == reply[1]:
        text = "Неплохо!"
    else:
        text = "Вы даже книгу не открывали!!!"
    bot.send_message(answer.chat.id, text)
    game_start(answer, reply_text='Продолжим игру')

'''
@bot.callback_query_handler(func = lambda call: call.data=='3')
def call_back_request(call):
    n = int(call.data)
    answer = bot.send_message(call.message.chat.id, question[n])
    bot.register_next_step_handler(answer, go_answer2)

def go_answer2(answer):
    if answer.text.lower() == reply[3]:
        text = "Да, это я!"
    else:
        text = "Вы точно со мной не знакомы..."
    bot.send_message(answer.chat.id, text)
    game_continue(answer)
'''

if __name__ == '__main__':
    bot.infinity_polling()