#!/usr/bin/env python3
#


import socket

messages = [b'this is conversation 1',
            b'this is conversation 2',
            b'this is conversation 2']

server_address = ('192.168.250.16', 9000)

socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(5)]

print('connect to %s:%s', server_address)
for s in socks:
    s.connect(server_address)

for m in messages:
    for s in socks:
        print('%s, sending "%s"', (s.getsockname(), m))
        s.send(m)

    for s in socks:
        data = s.recv(1024)
        print('%s, received "%s"', (s.getsockname(), data))
        if not data:
            print('closing socket ', s.getsockname())
