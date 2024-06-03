'''main.py

User code should start in here. This file takes the place of code.py from the default CPy behavior.
'''
import microcontroller
import time
import board
import supervisor
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.D5)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

i = 0
while True:
    print(f"({i}):Hello World!")
    i = i + 1
    if i > 9:
        i = 0
    if not btn.value:
        print("BTN is down")
        #microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
        #microcontroller.reset()
    else:
        print("BTN is up")
        
    time.sleep(1)
