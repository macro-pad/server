import uvicorn
from config import config
from api import api

uvicorn.run(api.app, host=config.host, port=config.port)

