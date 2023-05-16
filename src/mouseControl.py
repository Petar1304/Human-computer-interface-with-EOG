'''
  # commands
    - blink     ->  click
    - look left ->  left
    - look righ ->  right
    - look up   ->  mouse up
    - look down ->  mouse down
'''
import time
import pyautogui

pyautogui.FAILSAFE = False

def runCommand(command):
    stride = 50 # number of pixels to move
    timestamp = 0.2 # seconds

    if command == 'LEFT':
        pyautogui.dragRel(stride, 0, duration=timestamp)

    elif command == 'RIGHT':
        pyautogui.dragRel(-stride, 0, duration=timestamp)

    elif command == 'UP':
        pyautogui.dragRel(0, -stride, duration=timestamp)

    elif command == 'DOWN':
        pyautogui.dragRel(0, stride, duration=timestamp)

    elif command == 'CLICK':
        pos = pyautogui.position()
        pyautogui.leftClick(pos.x, pos.y)

