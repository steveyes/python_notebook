#!/usr/bin/env python3
#


import time


def consumer():
    while True:
        recv_data = yield True
        print("in consumer:", recv_data)


def producer():
    g = consumer()  # 切换到consumer
    next(g)

    for i in range(10):
        is_recv = g.send(i)
        print("in producer: ", is_recv)


start = time.time()
print("-----job start-----")
producer()
print(time.time() - start)
