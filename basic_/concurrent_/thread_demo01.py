#!/usr/bin/env python3
#


import time
import random
import threading


def eat(name):
    print(f'thread: {threading.current_thread()}, {name} eating ')
    time.sleep(random.randrange(1, 5))
    print(f'thread: {threading.current_thread()}, {name} eating ')


if __name__ == '__main__':
    t1 = threading.Thread(target=eat, args=('alice',))
    t1.start()
    print(f"main thread: {threading.current_thread()}")
