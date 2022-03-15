import random
import requests
import misc
import telebot
from telebot import types

token = misc.token
bot = telebot.TeleBot(token)


def get_total_confirmed():
    url = 'https://api.covid19api.com/summary'
    r = requests.get(url)
    b = []
    res = r.json()['Countries']
    for i in res:
        if i['Country'] == 'Belarus':
            b.append(i)
    return b[0]['TotalConfirmed']


def get_quote():
    url = 'https://www.breakingbadapi.com/api/quotes'
    r = requests.get(url)
    res = r.json()[random.randint(1, 100)]
    return res['quote']


def get_diy():
    url = 'http://www.boredapi.com/api/activity?type=diy'
    r = requests.get(url)
    res = r.json()
    return res['activity']


def get_joke():
    url = 'https://geek-jokes.sameerkumar.website/api?format=json'
    r = requests.get(url)
    res = r.json()
    return res['joke']


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Шутка')
    item2 = types.KeyboardButton('Цитата')
    item3 = types.KeyboardButton('Рандомная задача')
    item4 = types.KeyboardButton('Количество заболевших в РБ')

    markup.add(item1, item2, item3, item4)

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


bot.infinity_polling()
