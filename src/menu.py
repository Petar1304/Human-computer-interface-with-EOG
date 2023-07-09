from calibration import calibrate
from analysis import useMouse
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

while True:
    print(Fore.GREEN + '''
    Select option:
    1) calibration
    2) use mouse
    3) quit
    ''')
    command = input(Fore.BLUE + 'Command:\n>> ')
    if command == '1':
        calibrate()
    elif command == '2':
        useMouse()
    elif command == '3': break
    else:
        print(Fore.RED + 'Wrong command')

