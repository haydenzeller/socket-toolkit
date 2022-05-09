from ast import excepthandler
import socket
from requests import get

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

def ipcheck():
    try:
        ip = get('https://api.ipify.org').content.decode('utf8')
        print(bcolors.OKGREEN + "Your Public IP Address is: " + bcolors.WARNING + ip + bcolors.ENDC)
    except:
        print(bcolors.FAIL + "You are not connected to the internet." + bcolors.ENDC)