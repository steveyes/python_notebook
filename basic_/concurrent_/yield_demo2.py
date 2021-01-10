#!/usr/bin/env python3
#


import time


def consumer():
    while True:
        recv = yield True
        print(recv)


def producer():
    g = consumer()  # 切换到consumer
    next(g)
    for i in range(100000):
        is_recv = g.send(i)
        print(is_recv)


start = time.time()
producer()
print(time.time() - start)
