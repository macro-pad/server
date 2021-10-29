import os
import json

#TODO also allow to set path in env var
def load_config():
    f = open('../config.json')
    config = json.load(f)
    f.close()
    return config


def get_path(file):
    return os.path.abspath('../' + file)


config  = load_config()
grid    = get_path(config["grid"])
actions = get_path(config["actions"])
