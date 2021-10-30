from pykeyboard import PyKeyboard

def run(value):
    k = PyKeyboard()

    k.press_key(k.control_l_key)
    k.tap_key('1')
    k.tap_key('2')
    k.tap_key('3')
    k.release_key(k.control_l_key)
