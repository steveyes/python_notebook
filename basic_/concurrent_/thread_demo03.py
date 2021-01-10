#!/usr/bin/env python3
#


from threading import Thread
import threading
from multiprocessing import Process
import os


def work():
    import time
    time.sleep(3)
    print('sub thread:\t', threading.current_thread().getName())


if __name__ == '__main__':
    t = Thread(target=work)
    t.start()

    print('current thread name:\t', threading.current_thread().getName())
    print('current thread:\t', threading.current_thread())
    print('thread(s):\t', threading.enumerate())
    print('num of thread(s):\t', threading.active_count())
