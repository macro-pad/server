from pykeyboard import PyKeyboard

def run(value):
    k = PyKeyboard()

    k.press_key(k.control_l_key)
    k.press_key('1')
    k.press_key('2')
    k.press_key('3')
    k.release_key(k.control_l_key)
    k.release_key('1')
    k.release_key('2')
    k.release_key('3')
