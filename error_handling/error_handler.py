from datetime import datetime
from types import CellType

def create_error_log(text):
    # sys.path.append('')
    f = open("../error_handling/error_log.txt", "a+")
    f.write(str(datetime.now()))
    f.write('\t')
    f.write(text)
    f.write('\n')
    f.close()