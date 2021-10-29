import sys
sys.path.append('../plugins')

from fastapi import FastAPI
import data
import models
import plugin_caller

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

