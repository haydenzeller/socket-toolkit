import os
from selectors import EpollSelector
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

def scan():
    ip = input(bcolors.OKCYAN + 'ip address: ' + bcolors.ENDC)
    port = input(bcolors.OKCYAN + 'port (or "d" for default ): ' + bcolors.ENDC)
    os.system('clear')

    if port == 'd':
        print(bcolors.OKGREEN + 'Scanning ip address...' + bcolors.ENDC)
        os.system('sudo nmap -Pn --script vuln ' + ip)
        input(bcolors.OKGREEN + 'Press enter to return to the main menu.' + bcolors.ENDC)
        
    elif port != '':
        print(bcolors.OKGREEN + 'Scanning ip address...' + bcolors.ENDC)
        os.system('sudo nmap -Pn --script vuln -p ' + port + ' ' + ip)
        input(bcolors.OKGREEN + 'Press enter to return to the main menu.' + bcolors.ENDC)
    else:
        input(bcolors.FAIL + 'Invalid input. Press enter to return to main menu.' + bcolors.ENDC)