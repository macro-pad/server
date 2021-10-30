from datetime import datetime

def create_error_log(text):
    f = open("error.log", "a+")
    f.write(str(datetime.now()))
    f.write('\t')
    f.write(text)
    f.write('\n')
    f.close()
