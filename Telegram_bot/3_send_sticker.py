import telebot

# t.me/academy_shag_test456bot
API_TOKEN = '1163922176:AAGW3cNqBECqI_tqM1UPrEyWrXvQta__uP8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.chat.id, 'ID стикера: ' + message.sticker.file_id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOlXiwNQsF4GSbzHi4hWVEXKLqSYBIAAjYAAwxqnxLNzsAK-wEexBgE')

bot.polling()