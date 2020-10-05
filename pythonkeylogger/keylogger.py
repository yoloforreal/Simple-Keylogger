from pynput.keyboard import Key, Listener
from datetime import datetime

txtfile = input('Type in your text file location: ')
#print(datetime.now())

def on_press(key):
    f = open(txtfile, "a")
    f.write('{0} pressed'.format(
        key))
    f.close()

def on_release(key):
    g = open(txtfile, "a")
    g.write('{0} release'.format(
        key))
    if key == Key.esc:

        return False


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()