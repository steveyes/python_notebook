#!/usr/bin/env python3
#

import socket
from socket import AF_INET, SOCK_STREAM
from os import popen
from typing import List


def cond(arg: str) -> List[bool]:
    return [0 < len(arg) <= 1024, arg.upper() != 'EXIT', arg.upper() != 'QUIT', ]


server = socket.socket(AF_INET, SOCK_STREAM)

server.bind(('0.0.0.0', 9999))
server.listen()

while True:
    # 为每个新的client分配一个session
    conn, addr = server.accept()

    while True:
        print("new client: {} connected.".format(addr))
        recv = conn.recv(1024).decode()
        print('recv : {} : {}'.format(len(recv), recv))
        if all(cond(recv)):
            res = popen(recv).read()
            print('res : size : {}'.format(len(res)))
            if len(res) == 0:
                conn.send(('Oops, command not found: {}'.format(recv)).encode())
            conn.send(res.encode())
        else:
            print('client: {}, quiting....'.format(addr))
            conn.send(''.encode())
            break
