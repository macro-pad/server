import importlib.util
import json
import os
from config import config
from error_handling import error_handler
import threading

def get_pluginname(id):
    try:
        f = open(config.actions)
        actions = json.load(f)
        f.close()
        return actions[str(id)]
    except:
        return 0

def call_plugin(id, value = None):
    action = get_pluginname(id)
    if id == 0:
        error_handler.create_error_log('Button id not found')
        return 0
    try:
        custom_plugin_folder = os.path.abspath(config.plugin_dir + '/' + str(action["script"]))
        spec   = importlib.util.spec_from_file_location(action["script"], custom_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
    except:
        standart_plugin_folder = os.path.abspath('plugins/' + str(action["script"]))
        spec   = importlib.util.spec_from_file_location(action["script"], standart_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
    finally:
        if "async" in action:
            asyncThread = threading.Thread(target=plugin.run)
            try:
                if "params" in action:
                    asyncThread.start(value, action["params"])
                else:
                    asyncThread.start(value)
            except:
                error_handler.create_error_log('Error in plugin execution')
        else:
            try:
                if "params" in action:
                    return plugin.run(value, action["params"])
                else:
                    return plugin.run(value)
            except:
                error_handler.create_error_log('Error in plugin execution')