import random
import requests
import misc
import telebot

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


@bot.message_handler(commands=['total'])
def bot_message(message):
    bot.send_message(message.chat.id, f'Всего заболевших в Республике Беларусь: {get_total_confirmed()}')


@bot.message_handler(commands=['quote'])
def bot_quote(message):
    bot.send_message(message.chat.id, f'Держи цитату: {get_quote()}')


@bot.message_handler(commands=['diy'])
def bot_diy(message):
    bot.send_message(message.chat.id, f'Твоя задача на ближайшее время: {get_diy()}')


@bot.message_handler(commands=['joke'])
def bot_joke(message):
    bot.send_message(message.chat.id, f'Разрывная шутка: {get_joke()}')


bot.infinity_polling()
