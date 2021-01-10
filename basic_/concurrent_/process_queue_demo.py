#!/usr/bin/env python3
#


from multiprocessing import Process, Queue
import threading


def func(qq: Queue):
    print('in child, Queue.size():', qq.qsize())
    qq.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    q.put('45')
    p = Process(target=func, args=(q,))
    p.start()
    p.join()
    print("Queue.get_nowait():", q.get_nowait())
    print("Queue.get_nowait():", q.get_nowait())
    try:
        print("Queue.get_nowait():", q.get_nowait())
    except Exception as e:
        print(e)
