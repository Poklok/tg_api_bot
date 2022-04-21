import random
import requests


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


def get_data_car():
    url = 'http://127.0.0.1:8000/api/cars'
    r = requests.get(url)
    res_list = []
    res = r.json()
    for i in res:
        res_list.append(i['name_model_car'])
    return res_list
