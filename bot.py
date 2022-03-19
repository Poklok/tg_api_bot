from data import *
import misc
import telebot
from telebot import types

token = misc.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Шутка')
    item2 = types.KeyboardButton('Цитата')
    item3 = types.KeyboardButton('Рандомная задача')
    item4 = types.KeyboardButton('Количество заболевших в РБ')
    item5 = types.KeyboardButton('Модели машин')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Шутка':
            bot.send_message(message.chat.id, f'Разрывная шутка: {get_joke()}')
        elif message.text == 'Цитата':
            bot.send_message(message.chat.id, f'Держи цитату: {get_quote()}')
        elif message.text == 'Количество заболевших в РБ':
            bot.send_message(message.chat.id, f'Всего заболевших в Республике Беларусь: {get_total_confirmed()}')
        elif message.text == 'Рандомная задача':
            bot.send_message(message.chat.id, f'Твоя задача на ближайшее время: {get_diy()}')
        elif message.text == 'Модели машин':
            bot.send_message(message.chat.id, f'Модели машин: {get_data_car()}')


bot.infinity_polling()
