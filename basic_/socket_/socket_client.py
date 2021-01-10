#!/usr/bin/env python3
#


import socket
import sys

client = socket.socket()

client.connect(('192.168.250.16', 9999))


def cond_cont(arg):
    return len(arg) == 1024


def cond_last(arg):
    return 0 < len(arg) < 1024


def cond_null(arg):
    return len(arg) == 0


while True:
    cmd = input(">>> ").strip()

    if not cmd: continue

    if cmd.lower() in ['exit', 'quit']:
        client.send(''.encode())
        sys.exit(0)

    client.send(cmd.encode())
    res = ''
    while True:
        recv = client.recv(1024).decode()
        if cond_cont(recv):
            res += recv
        elif cond_last(recv):
            res += recv
            break
        elif cond_null(recv):
            client.send('exit'.encode())
            break
        else:
            # client.send('exit'.encode())
            break
    print(res)
