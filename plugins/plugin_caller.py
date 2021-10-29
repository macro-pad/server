import sys
sys.path.append('../config')
import importlib.util
import json
import os
import config
import error_handling

def get_pluginname(id):
    try:
        f = open(config.actions)
        actions = json.load(f)
        f.close()
        return actions[str(id)]
    except:
        return 0

def call_plugin(id, param = None):
    plugin_name = get_pluginname(id)
    if id == 0:
        error_handling.create_error_log('Button id not found')
        return 0
    try:
        custom_plugin_folder = os.path.abspath(config.plugin_dir + '/' + plugin_name)
        spec   = importlib.util.spec_from_file_location(plugin_name, custom_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
    except:
        standart_plugin_folder = os.path.abspath('../plugins' + '/' + str(plugin_name))
        spec   = importlib.util.spec_from_file_location(plugin_name, standart_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
    finally:
        try:
            if param != None:
                plugin.run(param)
            else:
                plugin.run()
        except:
            error_handling.create_error_log('Error in plugin execution')

call_plugin(1)