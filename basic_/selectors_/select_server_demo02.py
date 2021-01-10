#!/usr/bin/env python3
#


import queue
import select
import socket

server = socket.socket()
server.bind(('192.168.250.203', 9000))
server.listen(2048)  # 队列大小
server.setblocking(False)  # 不阻塞
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # TIME WAIT reuse
print('starting...')

rlist = [server, ]
wlist = []
wqueue = {}

while True:
    read_list, write_list, except_list = select.select(rlist, wlist, rlist)

    # 当前有活动的读事件的连接
    print(f"read_list: {read_list}")
    for r in read_list:

        # 如果是首次握手
        if r is server:
            conn, addr = r.accept()

            # 将该连接加入 rlist 监控
            print('new accept: ', addr)
            rlist.append(conn)

            # 为该连接分配一个 queue
            wqueue[conn] = queue.Queue()

        # 如果不是首次握手
        else:
            try:
                data = r.recv(1024)
                # 没有收到数据，就关闭连接，
                # 并将其从 rlist 中移除
                # 并将其 queue 删除
                # 然后处理下一个 rlist 中活动的连接
                if not data or data.upper() == "exit".upper():
                    r.close()
                    rlist.remove(r)
                    del wqueue[r]
                    continue

                # 将该连接加入 wlist
                wlist.append(r)

                # 准备返回给对端的数据
                wqueue[r].put(data.upper())

            except Exception:
                r.close()
                rlist.remove(r)

    # 当前有活动的写事件的连接
    print(f"write_list: {write_list}")
    for w in write_list:
        print(f"wqueue[w].qsize(): {wqueue[w].qsize()}")
        print(f"is w in wqueue: { w in wqueue}")
        # 发送消息
        w.send(wqueue[w].get())

        # 消息发送完毕，从 wlist 中移除
        wlist.remove(w)

        print(f"wqueue[w].qsize(): {wqueue[w].qsize()}")
        print(f"is w in wqueue: { w in wqueue}")

    # 当前有异常的连接
    for e in except_list:
        print(f"exception: {e}")
        if e in wlist:
            wlist.remove(e)
        rlist.remove(e)
        del wqueue[e]

    print()
    print("-----> QUEUE <-----")
    for k, v in wqueue.items():
        # 存活的 queue 的大小就相当于存活的 tcp 连接数
        print(v.qsize())
    print("-----< QUEUE >-----")
    print()
