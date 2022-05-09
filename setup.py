import os
import sys
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

print(bcolors.OKGREEN +'''
   _____            _        _     _______          _ _    _ _   
  / ____|          | |      | |   |__   __|        | | |  (_) |  
 | (___   ___   ___| | _____| |_     | | ___   ___ | | | ___| |_ 
  \___ \ / _ \ / __| |/ / _ \ __|    | |/ _ \ / _ \| | |/ / | __|
  ____) | (_) | (__|   <  __/ |_     | | (_) | (_) | |   <| | |_ 
 |_____/ \___/ \___|_|\_\___|\__|    |_|\___/ \___/|_|_|\_\_|\__|'''
 + bcolors.ENDC)
print(bcolors.WARNING + 'This script will automatically install all the necessary dependencies for the project.')
print(' ')
input('Press enter to continue...' + bcolors.ENDC)

os.system('sudo apt-get install nmap')
os.system('sudo apt-get update && sudo apt-get upgrade -y')
os.system('sudo apt-get install python3-pip -y')
os.system('sudo apt-get install git -y')
os.system('git clone https://github.com/Und3rf10w/kali-anonsurf.git')
os.chdir('kali-anonsurf')
os.system('chmod +x installer.sh')
os.system('sudo ./installer.sh')
os.chdir('..')
os.system('sudo rm -R kali-anonsurf')
os.system('pip3 install requests')
os.system('pip3 install paramiko colorama')

input(bcolors.OKGREEN + '''Done! Please run stk.py or open a new shell and type stk to start the program!
Press enter to exit.''' + bcolors.ENDC)