# 1 = click, 2 = jump, 3 = jitter, 4 = walk in square, 5 = spin
mode = 4

import pydirectinput
import keyboard
import time

afk = False
while True:
    if keyboard.is_pressed('q'):
        afk = True
    while afk:
        if mode == 1:
            # DON'T CHANGE THIS FROM 1 IT WILL NO GO WELL
            pydirectinput.click(interval=1)
        elif mode == 2:
            pydirectinput.press(' ', _pause=False)
        elif mode == 3:
            pydirectinput.press('w', _pause=False)
            pydirectinput.press('d', _pause=False)
            pydirectinput.press('s', _pause=False)
            pydirectinput.press('a', _pause=False)
        elif mode == 4:
            pydirectinput.keyDown('w')
            time.sleep(1)
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('d')
            time.sleep(1)
            pydirectinput.keyUp('d')
            pydirectinput.keyDown('s')
            time.sleep(1)
            pydirectinput.keyUp('s')
            pydirectinput.keyDown('a')
            time.sleep(1)
            pydirectinput.keyUp('a')
        elif mode == 5:
            pydirectinput.moveTo(980, 540)
        
            