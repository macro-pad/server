import requests

def run(value):
    request = requests.get('https://api.openweathermap.org/data/2.5/weather?q=St.%20Gallen&appid=92b6b47a3146d720b6bb622ce7f1583c')
    json = request.json()
    return json[value]
