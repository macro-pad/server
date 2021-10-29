import json
import sys
import os

with open("actions.json") as json_data_file:
    buttonMappingConfig = json.load(json_data_file)

root_directory = os.getcwd()
standart_plugin_folder = os.path.abspath('./plugins')
custom_plugin_folder   = os.path.abspath('./customPlugins')

def get_pluginname(id):

    try:
        return buttonMappingConfig[str(id)]
    except:
        return 0

def call_plugin(id, param = None):
    plugin_name = get_pluginname(id)
    print(plugin_name)
    # os.chdir(standart_plugin_folder)

    # a = os.getcwd()
    # print(a)

    # exec(plugin_name)
    # os.chdir(root_directory)

call_plugin(1)