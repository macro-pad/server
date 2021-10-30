import os
import json


def load_config():
    f = open(os.environ.get('MACRO-PAD_CONFIG', 'config.json'))
    config = json.load(f)
    f.close()
    return config


def get_path(relative_path):
    return os.path.abspath(relative_path)


config      = load_config()

host        = config["host"]
port        = config["port"]
grid        = get_path(config["grid"])
actions     = get_path(config["actions"])
plugin_dir  = get_path(config["plugin_dir"])
