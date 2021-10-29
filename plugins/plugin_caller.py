import importlib.util
import json
import sys
import os

with open("actions.json") as json_data_file:
    buttonMappingConfig = json.load(json_data_file)


def get_pluginname(id):

    try:
        return buttonMappingConfig[str(id)]
    except:
        return 0

def call_plugin(id, param = None):
    plugin_name = get_pluginname(id)
    if id == 0:
        #TODO: errorhandling
        log = 'Id not found'
    try:
        custom_plugin_folder   = os.path.abspath('../customPlugins' + '\\' + plugin_name)
        spec   = importlib.util.spec_from_file_location(plugin_name, custom_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
        # plugin.run()
    except:
        standart_plugin_folder = os.path.abspath('./' + plugin_name)
        spec   = importlib.util.spec_from_file_location(plugin_name, standart_plugin_folder)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)

        
    


call_plugin(1)