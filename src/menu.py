from calibration import calibrate


while True:
    print('''
    Select option:
    1) calibration
    2) run
    3) quit
    ''')
    command = input('Enter Command\n>> ')
    if command == '1':
        calibrate()
    elif command == '2':
        pass
    elif command == '3': break
    else:
        print('Wrong command')