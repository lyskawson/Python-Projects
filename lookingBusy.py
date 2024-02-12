#!/usr/bin/env python3


import time
import pyautogui

print('NudgeBot activated, press CTRL-C to quit.')
try:
    while True:
        pyautogui.moveRel(0, -200, 0.5)
        pyautogui.moveRel(-100, 0, 0.5)
        ćpyautogui.moveRel(0, 200, 0.5)
        pyautogui.moveRel(100, 0, 0.5)

        time.sleep(10)
except KeyboardInterrupt:
    print(' NudgeBot deactivated.')