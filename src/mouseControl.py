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
DURATION = 0.01 # seconds

def runCommand(commands):
    axis1_com, axis2_com = commands
    
    if axis1_com == 'RIGHT':
        pyautogui.moveRel(STRIDE, 0, duration=DURATION)
    elif axis1_com == 'LEFT':
        pyautogui.moveRel(-STRIDE, 0, duration=DURATION)

    if axis2_com == 'UP':
        pyautogui.moveRel(0, -STRIDE, duration=DURATION)
    elif axis2_com == 'DOWN':
        pyautogui.moveRel(0, STRIDE, duration=DURATION)

    elif command == 'CLICK':
        pos = pyautogui.position()
        pyautogui.leftClick()
