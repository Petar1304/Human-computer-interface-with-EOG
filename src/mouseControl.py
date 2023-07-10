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

# HYPERPARAMETERS
STRIDE = 50 # number of pixels to move
DURATION = 0.5 # seconds

def runCommand(commands):
    axis1_com, axis2_com = commands
    # print(pyautogui.position())

    if axis2_com == 'RIGHT':
        pyautogui.move(STRIDE, 0)
    elif axis2_com == 'LEFT':
        pyautogui.move(-STRIDE, 0)

    if axis1_com == 'UP':
        pyautogui.move(0, -STRIDE)
    elif axis1_com == 'DOWN':
        pyautogui.move(0, STRIDE)

    # elif command == 'CLICK':
    #     pyautogui.leftClick()
