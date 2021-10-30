import webbrowser
import threading
def run():
    link = 'https://github.com/'
    webbrowser.open(link)
    print('abc')

print('a')
x = threading.Thread(target=run)
print('b')
x.start()
print('c')