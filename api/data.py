import sys
sys.path.append('../config')

import json
import config

def get_grid():
    f = open(config.grid)
    grid = json.load(f)
    f.close()
    return grid


