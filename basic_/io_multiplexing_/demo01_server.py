#!/usr/bin/env python3
#


'''

Create an epoll object——创建1个epoll对象
Tell the epoll object to monitor specific events on specific sockets——告诉epoll对象，在指定的socket上监听指定的事件
Ask the epoll object which sockets may have had the specified event since the last query——询问epoll对象，从上次查询以来，哪些socket发生了哪些指定的事件
Perform some action on those sockets——在这些socket上执行一些操作
Tell the epoll object to modify the list of sockets and/or events to monitor——告诉epoll对象，修改socket列表和（或）事件，并监控
Repeat steps 3 through 5 until finished——重复步骤3-5，直到完成
Destroy the epoll object——销毁epoll对象
'''

'''
import select 导入select模块

epoll = select.epoll() 创建一个epoll对象

epoll.register(文件句柄,事件类型) 注册要监控的文件句柄和事件

事件类型:

　　select.EPOLLIN    可读事件

　　select.EPOLLOUT   可写事件

　　select.EPOLLERR   错误事件

　　select.EPOLLHUP   客户端断开事件

epoll.unregister(文件句柄)   销毁文件句柄

epoll.poll(timeout)  当文件句柄发生变化，则会以列表的形式主动报告给用户进程,timeout

                     为超时时间，默认为-1，即一直等待直到文件句柄发生变化，如果指定为1

                     那么epoll每1秒汇报一次当前文件句柄的变化情况，如果无变化则返回空

epoll.fileno() 返回epoll的控制文件描述符(Return the epoll control file descriptor)

epoll.modfiy(fineno,event) fineno为文件描述符 event为事件类型  作用是修改文件描述符所对应的事件

epoll.fromfd(fileno) 从1个指定的文件描述符创建1个epoll对象

epoll.close()   关闭epoll对象的控制文件描述符
'''

import socket
import select
import queue

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("0.0.0.0", 8888)
server_socket.bind(server_address)
server_socket.listen(10)
print("server start, listening: ", server_address)
server_socket.setblocking(False)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
timeout = 10
epoll = select.epoll()

# 注册服务器监听fd到等待读事件集合
epoll.register(server_socket.fileno(), select.EPOLLIN)

# 保存连接客户端消息的字典，格式为{}
message_queues = {}

# 文件句柄到所对应对象的字典，格式为{句柄：对象}
fd_to_socket = {server_socket.fileno(): server_socket, }

while True:
    print('wait for new connection...')
    events = epoll.poll(timeout)
    if not events:
        print('epoll time out, no ready connection, round robin again...')
        continue
    print(f'now coming {len(events)} new event, start to handle...')

    for fd, event in events:
        sock = fd_to_socket[fd]

        # 如果活动 socket 为当前服务器 socket， 表示有新的连接
        if sock == server_socket:
            connection, address = server_socket.accept()
            print('new connection: ', address)
            connection.setblocking(False)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # 注册新连接fd到待读事件集合
            epoll.register(connection.fileno(), select.EPOLLIN)

            # 把新连接的文件句柄以及对象保存到字典
            fd_to_socket[connection.fileno()] = connection

            message_queues[connection] = queue.Queue()

        # 关闭事件
        elif events and select.EPOLLHUP:
            print('client close')
            epoll.unregister(fd)
            fd_to_socket[fd].close()
            del fd_to_socket[fd]

        # 可读事件
        elif event and select.EPOLLIN:
            data = sock.recv(1024)
            if data:
                print("recv: ", data, "client: ", sock.getpeername())

                # 将数据放入对应客户端的字典
                message_queues[sock].put(data)

                # 修改读取到消息的连接到等待写事件集合(即对应客户端收到消息后，再将其fd修改并加入写事件集合)
                epoll.modify(fd, select.EPOLLOUT)

        # 可写事件
        elif event and select.EPOLLOUT:
            try:
                # 从字典中获取对应客户端的信息
                msg = message_queues[sock].get_nowait()
            except queue.Empty:
                print(sock.getpeername(), " queue empty")
                # 修改文件句柄为读事件
                epoll.modify(fd, select.EPOLLIN)
            else:
                print("发送数据：", data, "客户端：", sock.getpeername())
                # 发送数据
                sock.send(msg)

# 在epoll中注销服务端文件句柄
epoll.unregister(serversocket.fileno())
# 关闭epoll
epoll.close()
# 关闭服务器socket
serversocket.close()
