#!/usr/bin/env python3
#


from multiprocessing import Process, Pipe
import os


# 子进程
def f(conn):
    conn.send([f'ppid: {os.getppid()}', f'pid: {os.getpid()}', None, 'hello from child'])
    print("from parent", conn.recv())
    conn.close()


# 主进程
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print("from child", parent_conn.recv())
    parent_conn.send([f'ppid: {os.getppid()}', f'pid: {os.getpid()}', None, "hello from parent"])
    p.join()
