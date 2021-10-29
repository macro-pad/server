import os
import json

#TODO also allow to set path in env var
def load_config():
    f = open('../config.json')
    config = json.load(f)
    f.close()
    return config

def get_path(relative_path):
    return os.path.abspath('../' + relative_path)


config      = load_config()
grid        = get_path(config["grid"])
actions     = get_path(config["actions"])
plugin_dir  = get_path(config["plugin_dir"])

print(plugin_dir)