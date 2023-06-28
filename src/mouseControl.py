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

    if command == 'RIGHT':
        pyautogui.moveRel(stride, 0, duration=timestamp)
    
    elif command == 'LEFT':
        pyautogui.moveRel(-stride, 0, duration=timestamp)

    elif command == 'UP':
        pyautogui.moveRel(0, -stride, duration=timestamp)

    elif command == 'DOWN':
        pyautogui.moveRel(0, stride, duration=timestamp)

    elif command == 'CLICK':
        # pos = pyautogui.position()
        pyautogui.leftClick()

# testing
# while True:
#     runCommand('RIGHT')
#     runCommand('CLICK')
#     time.sleep(1)