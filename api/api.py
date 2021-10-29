from fastapi import FastAPI
import data

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/grid")
def get_grid():
    return {"grid": data.get_grid()}
