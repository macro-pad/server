from fastapi import FastAPI
from plugins import plugin_caller
from api import models
from api import data

app = FastAPI()


@app.get("/grid")
def get_grid():
    return data.get_grid()


@app.post("/action/{id}")
def action(id, action: models.Action):
    plugin_response = plugin_caller.call_plugin(id, action.value)
    if plugin_response == True:
        return {"status": "success"}

    return {"status": "error", "error": plugin_response}

