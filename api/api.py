from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from plugins import plugin_caller
from api import models
from api import data
import requests
import json
import time
app = FastAPI()


@app.get("/grid")
def get_grid():
    return data.get_grid(1)


@app.post("/action/{id}")
def action(id, action: models.Action):
    plugin_response = plugin_caller.call_plugin(id, action.value)
    if plugin_response:
        return plugin_response


html = """ <p> Hello World <p> """

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # time.sleep(1)
        weather_json = requests.get('https://api.github.com/user', auth=('pass'))
        # config = json.load(weather_json)
        # print(weather_json)
        await websocket.send_text("<h2>HelloWorld</h2>")