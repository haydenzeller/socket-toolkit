#IMPORTS
from ast import excepthandler
import sys
import os
import time
import socket
import modules.ipcheck
import modules.ipscan
#IMPORTS

#CLASSES
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKCYAN = '\033[96m'
#CLASSES

#Title and disclaimer
print(bcolors.OKGREEN + '''
   _____            _        _     _______          _ _    _ _   
  / ____|          | |      | |   |__   __|        | | |  (_) |  
 | (___   ___   ___| | _____| |_     | | ___   ___ | | | ___| |_ 
  \___ \ / _ \ / __| |/ / _ \ __|    | |/ _ \ / _ \| | |/ / | __|
  ____) | (_) | (__|   <  __/ |_     | | (_) | (_) | |   <| | |_ 
 |_____/ \___/ \___|_|\_\___|\__|    |_|\___/ \___/|_|_|\_\_|\__|
                                                                 ''' + bcolors.ENDC)
print(bcolors.FAIL + '''DISCLAIMER:
  This script is not intended to be used for malicious purposes.
  it was made puplic for educational purposes only
  and has no warranties or guarantees.''' + bcolors.ENDC)
terms = input(bcolors.WARNING + 'Do you accept the terms of use? Y/n: ' + bcolors.ENDC)
if terms == 'Y' or terms == 'y' or terms == 'yes' or terms == 'Yes' or terms == 'YES' or terms == '':
    os.system('clear')
    print(bcolors.OKGREEN + 'Terms accepted.' + bcolors.ENDC)
elif terms == 'N' or terms == 'n' or terms == 'no' or terms == 'No' or terms == 'NO':
    os.system('clear')
    print(bcolors.FAIL + 'Terms not accepted. Exiting...' + bcolors.ENDC)
    time.sleep(1)
    sys.exit()
else:
    os.system('clear')
    print(bcolors.FAIL + 'Invalid input. Exiting...' + bcolors.ENDC)
    time.sleep(1)
    sys.exit()
#TITLE AND DISCLAIMER

#MAIN SELECTION


def main():
    print(bcolors.OKGREEN + '''
  _____            _        _     _______          _ _    _ _   
 / ____|          | |      | |   |__   __|        | | |  (_) |  
| (___   ___   ___| | _____| |_     | | ___   ___ | | | ___| |_ 
 \___ \ / _ \ / __| |/ / _ \ __|    | |/ _ \ / _ \| | |/ / | __|
 ____) | (_) | (__|   <  __/ |_     | | (_) | (_) | |   <| | |_ 
|_____/ \___/ \___|_|\_\___|\__|    |_|\___/ \___/|_|_|\_\_|\__|
                                                                
                                                                    ''' + bcolors.ENDC)
    print(bcolors.WARNING + '''
    [1] Check my ip address     [2] Enable Anonsurf
    [3] Disable Anonsurf        [4] IP vulnerabilities check
    [5] SSH brute force
                        ''' + bcolors.ENDC)
    mainselection = input(bcolors.OKCYAN + 'Select an option: ' + bcolors.ENDC)
    if mainselection == '1':
        os.system('clear')
        print(bcolors.OKGREEN + 'Checking ip address...' + bcolors.ENDC)
        modules.ipcheck.ipcheck()
        input(bcolors.WARNING + 'Press enter to return to the main menu...' + bcolors.ENDC)
        os.system('clear')
        main()
    if mainselection == '2':
        os.system('clear')
        os.system('sudo anonsurf start')
        input(bcolors.WARNING + 'Press enter to return to the main menu...' + bcolors.ENDC)
        os.system('clear')
        main()
    if mainselection == '3':
        os.system('clear')
        os.system('sudo anonsurf stop')
        input(bcolors.WARNING + 'Press enter to return to the main menu...' + bcolors.ENDC)
        os.system('clear')
        main()
    if mainselection == '4':
        os.system('clear')
        modules.ipscan.scan()
        os.system('clear')
        main()
    if mainselection == '5':
        os.system('clear')

        print(bcolors.OKGREEN + '''
  _____ _____ _    _   ____  _____  _    _ _______ ______ 
 / ____/ ____| |  | | |  _ \|  __ \| |  | |__   __|  ____|
| (___| (___ | |__| | | |_) | |__) | |  | |  | |  | |__   
 \___ \\___ \|  __  | |  _ <|  _  /| |  | |  | |  |  __|  
 ____) |___) | |  | | | |_) | | \ \| |__| |  | |  | |____ 
|_____/_____/|_|  |_| |____/|_|  \_\\____/   |_|  |______|
                                                        ''' + bcolors.ENDC)
        ip = input(bcolors.WARNING + 'Enter an ip address: ' + bcolors.ENDC)
        username = input(bcolors.WARNING + 'Enter a username: ' + bcolors.ENDC)
        password = input(bcolors.WARNING + 'Path to passwordlist (Enter for default list): ' + bcolors.ENDC)
        if password == '':
            password = 'modules/passlist.txt'
            input(bcolors.OKCYAN + 'Press enter to start...' + bcolors.ENDC)
        try:
            os.system('sudo python3 modules/sshbrute.py -u ' + username + ' -P ' + password + ' ' + ip)
            input(bcolors.WARNING + 'Press enter to return to the main menu...' + bcolors.ENDC)
            os.system('clear')
            main()
        except:
            print(bcolors.FAIL + 'An error occured.' + bcolors.ENDC)
            input(bcolors.WARNING + 'Press enter to return to the main menu...' + bcolors.ENDC)
            main()

main()



