import importlib.util
import json
import os
from config import config

# custom_plugin_folder = os.path.abspath(''../plugins + '/' + plugin_name)
# spec   = importlib.util.spec_from_file_location(plugin_name, custom_plugin_folder)
# plugin = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(plugin)

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
    print(plugin_name)
    if id == 0:
        #TODO: errorhandling
        log = 'Id not found'
    try:
        custom_plugin_folder = os.path.abspath(config.plugin_dir + '/' + str(plugin_name))
        spec   = importlib.util.spec_from_file_location(plugin_name, custom_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
        # plugin.run()
    except:
        standart_plugin_folder = os.path.abspath('../plugins' + '/' + str(plugin_name))
        spec   = importlib.util.spec_from_file_location(plugin_name, standart_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
        