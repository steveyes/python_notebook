#!/usr/bin/env python3
#

import threading
import time
import queue

q = queue.Queue(maxsize=100)


def producer(name):
    count = 0
    while True:
        q.put(f"baozi[{count}]")
        print(f"{name} yield baozi[{count}]")
        count += 1
        time.sleep(1)


def consumer(name):
    while True:
        print(f"{name} get {q.get()}...")
        time.sleep(2)


if __name__ == '__main__':
    p1 = threading.Thread(target=producer, args=("alice",))
    p2 = threading.Thread(target=producer, args=("bob",))
    c1 = threading.Thread(target=consumer, args=('Grace',))
    c2 = threading.Thread(target=consumer, args=('Mallory',))
    c3 = threading.Thread(target=consumer, args=('Victor',))

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()
