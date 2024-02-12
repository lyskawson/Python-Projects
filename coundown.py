#! /usr/bin/env python3

import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1


subprocess.Popen(['open', '/Users/aleklyskawa/Desktop/examples/alarm.wav'])
