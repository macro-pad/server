import requests


weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=St.%20Gallen&appid=92b6b47a3146d720b6bb622ce7f1583c')
# print(weather_json)
# a = json.load(weather.json)
a = weather.json()
        
# b = a.json()
# a = 'abc'
# data = json.load(weather_json)
# await websocket.send_json(weather_json)
b = a["name"]
print(b)
print(a)