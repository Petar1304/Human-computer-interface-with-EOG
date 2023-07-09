from calibration import calibrate
from analysis import useMouse

while True:
    print('''
    Select option:
    1) calibration
    2) use mouse
    3) quit
    ''')
    command = input('Enter Command\n>> ')
    if command == '1':
        calibrate()
    elif command == '2':
        useMouse()
    elif command == '3': break
    else:
        print('Wrong command')

