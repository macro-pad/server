from api import data

def run(value, params):
    grid = data.get_grid(params['grid'])
    return grid