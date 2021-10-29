import sys
import json
from config import config

def get_grid(id):
    f = open(config.grid)
    grid = json.load(f)
    f.close()
    return grid[str(id)]
