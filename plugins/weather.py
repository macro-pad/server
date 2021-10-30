import requests

def run(value):
<<<<<<< HEAD
    weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=St.%20Gallen&appid=92b6b47a3146d720b6bb622ce7f1583c')
    json = weather.json()
    output = """
        {
            'name' :""" + json["name"]        + """
            'temp' :""" + json["temp"]-273.15 + """
            'speed':""" + json["speed"]       + """
        }
    """
    
    output += ','