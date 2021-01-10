#!/usr/bin/env python3
#

'''
fileobj: 注册的文件对象
fd: 底层的文件描述符
events: 文件对象必须等待的事件
data: 与文件对象相关联的数据, 例如可用来存储每个客户端的会话ID.

python要完成高并发需要协程,事件循环,高效IO模型.而Python自带的asyncio模块已经全部完成了.
'''

import selectors
import socket

sel = selectors.DefaultSelector()


# 创建一个新的 socket 模板
def NEW_SOCKET():
    sock = socket.socket()
    SERVER_ADDR = '192.168.250.16'
    SERVER_PORT = 9000
    BACKLOG = 10000

    sock.bind((SERVER_ADDR, SERVER_PORT))
    sock.listen(BACKLOG)

    # 设置 T 状CP态为 TIME_WAIT 时，端口依然可以重用。
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 设置非阻塞
    sock.setblocking(False)

    return sock


# 回调函数，用于接收新连接
def accept(sock: socket.socket, mask):
    conn, addr = sock.accept()
    print(f"accept: {conn}, from: {addr}, mask:{mask}\n")

    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


# 回调函数，用于读取 client 用户数据
def read(conn: socket.socket, mask):
    data = conn.recv(1024)
    if data:
        print(f"read: {repr(data)}, conn: {conn}, mask: {mask}")
        conn.send(data)
    else:
        print('closing: ', conn)
        print()
        sel.unregister(conn)
        conn.close()


def main():
    sock = NEW_SOCKET()
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        # 默认阻塞，有活动连接就返回会动的连接列表
        events = sel.select()

        # key是个selectorkey对象, 有属性fileobj, data, 等
        for key, mask in events:
            # 有新连接时：events 列表中有刚注册的回调函数 accept, 就存于 key.data 中
            # 已有连接时：events 列表中有 accept 函数中注册的 read 函数，就存于 key.data 中
            callback = key.data

            # 有新连接时：调用 callback 就等于 调用 key.data 就等于调用 accept
            # 已有连接时：调用 callback 就等于 调用 key.data 就等于调用 read
            callback(key.fileobj, mask)  # key.fileobj，文件句柄
        print(f"events: {events}")


if __name__ == '__main__':
    main()
