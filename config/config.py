import os
import json

#TODO also allow to set path in env var
def load_config():
    f = open('config.json')
    config = json.load(f)
    f.close()
    return config

<<<<<<< HEAD

def get_path(relative_path):
    return os.path.abspath(relative_path)
=======
def get_path(relativ_path):
    return os.path.abspath(relativ_path)
>>>>>>> 4f734b3834422870065530ae607b726218716ee1


config      = load_config()

host        = config["host"]
port        = config["port"]
grid        = get_path(config["grid"])
actions     = get_path(config["actions"])
plugin_dir  = get_path(config["plugin_dir"])
