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

def runCommand(commands):
    axis1_com, axis2_com = commands
    
    stride = 50 # number of pixels to move
    timestamp = 0.2 # seconds

    if axis1_com == 'RIGHT':
        pyautogui.moveRel(stride, 0, duration=timestamp)
    elif axis1_com == 'LEFT':
        pyautogui.moveRel(-stride, 0, duration=timestamp)

    if axis2_com == 'UP':
        pyautogui.moveRel(0, -stride, duration=timestamp)
    elif axis2_com == 'DOWN':
        pyautogui.moveRel(0, stride, duration=timestamp)

    elif command == 'CLICK':
        pos = pyautogui.position()
        pyautogui.leftClick()
