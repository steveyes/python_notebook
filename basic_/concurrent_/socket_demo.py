#!/usr/bin/env python3
#


import socket

import gevent


def server_run(server_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((server_ip, port))
    s.listen(5)
