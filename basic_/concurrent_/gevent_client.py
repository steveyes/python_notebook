#!/usr/bin/env python3
#


from threading import Thread
from socket import *
import threading
import time

# def client(server_ip, port):
#     c = socket(AF_INET, SOCK_STREAM)
#     c.connect((server_ip, port))
#
#     count = 0
#     while True:
#         c.send(('%s say hello %s' % (threading.current_thread().getName(), count)).encode('utf-8'))
#         msg = c.recv(1024)
#         print(msg.decode('utf-8'))
#         count+=1


def client(server_ip, port):
    c = socket(AF_INET, SOCK_STREAM)
    c.connect((server_ip, port))

    count = 0
    while True:
        time.sleep(1)
        talk(c, count)
        count += 1


def talk(conn, count):
    try:
        conn.send(('%s say hello %s' % (threading.current_thread().getName(), count)).encode('utf-8'))
        msg = conn.recv(1024)
        print(msg.decode('utf-8'))
    except Exception as e:
        raise Exception(e)
    finally:
        # 不能 conn.close()，否则报错：[WinError 10038] 在一个非套接字上尝试了一个操作，因为socket先close再调recv就会报错。
        pass


if __name__ == '__main__':
    server_ip = '192.168.250.203'
    server_port = 8080
    # 10个线程
    for i in range(10):
        t = Thread(target=client, args=(server_ip, server_port))
        t.start()
