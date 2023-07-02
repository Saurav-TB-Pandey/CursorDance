# Project name :- CursorDance
# Developer name :- Saurav Pandey
# Version :- 1.0v

import pyautogui as auto
from threading import Thread
from keyboard import is_pressed
from random import sample
from time import sleep
from sys import exit

def move():
    def moveCursor(x, y):
        auto.FAILSAFE = False
        auto.moveTo(x, y)

    number = "123456789"
    length = 3

    while True:
        x = "".join(sample(number, length))
        y = "".join(sample(number, length))

        moveCursor(int(x), int(y))

        # print(x, y)
        sleep(1)

# Create a daemon thread
thread = Thread(target=move)
thread.daemon = True

thread.start()

# Keep the main thread running
while True:
    if is_pressed('esc + space'):
        exit()