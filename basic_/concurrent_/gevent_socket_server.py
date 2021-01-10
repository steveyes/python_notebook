#!/usr/bin/env python3
#

from gevent import monkey

monkey.patch_all()

from socket import *
import gevent


def server_run(server_ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((server_ip, port))
    s.listen(500)
    while True:
        conn, addr = s.accept()
        gevent.spawn(talk, conn, addr)


def talk(conn: socket(), addr):
    try:
        while True:
            recv_data = conn.recv(1024)
            if recv_data:
                print('client %s:%s msg:%s' % (addr[0], addr[1], recv_data))
                conn.send(recv_data.upper())
            else:
                conn.close()
                break
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    server_ip = '192.168.250.203'
    server_port = 8080
    server_run(server_ip, 8080)

# def talk(conn: socket(), count):
#     try:
#         conn.send(('%s say hello %s' % (threading.current_thread().getName(), count)).encode('utf-8'))
#         msg = conn.recv(1024)
#         print(msg.decode('utf-8'))
#     except Exception as e:
#         raise Exception(e)
#     finally:
#         conn.close()
