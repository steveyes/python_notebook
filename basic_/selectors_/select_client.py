#!/usr/bin/env python3
#


from socket import *
import sys

c = socket(AF_INET, SOCK_STREAM)
c.connect(("192.168.250.203", 9000))

while True:
    msg = input('>>: ')
    if not msg: continue
    if msg.upper() == 'exit'.upper():
        sys.exit()

    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))
