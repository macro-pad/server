from os import name
import requests
import json

def run(value):
    request = requests.get('https://api.openweathermap.org/data/2.5/weather?q=St.%20Gallen&appid=92b6b47a3146d720b6bb622ce7f1583c')
    if value == 'name':
        return request.json()['name']
    if value == 'speed':
        return request.json()['wind']['speed']
    if value == 'temp':
        r = request.json()['main']['temp']
        return r-273,15