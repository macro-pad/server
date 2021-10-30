from io import StringIO
from fastapi import FastAPI
from pydantic import BaseModel

class Action(BaseModel):
    value: str