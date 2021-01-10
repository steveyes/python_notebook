#!/usr/bin/env python3
#


import time


def consumer():
    while True:
        res = yield


def producer():
    g = consumer()
    next(g)
    for i in range(1000000):
        g.send(i)


start = time.time()
producer()
print(time.time() - start)
