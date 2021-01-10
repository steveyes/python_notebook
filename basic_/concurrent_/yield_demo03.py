#!/usr/bin/env python3
#


import time
import queue


def consumer(name):
    print("--->staring eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))


def producer():
    r1 = cs1.__next__()
    r2 = next(cs2)
    r3 = cs3.send(None)
    n = 0
    print("--->staring making baozi<---")
    while n < 5:
        n += 1
        print('\033[32;1m[producer]\033[0m is making 3 baozi %s' % n)
        cs1.send(n)
        cs2.send(n)
        cs3.send(n)
        time.sleep(1)


if __name__ == '__main__':
    cs1 = consumer("c1")
    cs2 = consumer("c2")
    cs3 = consumer("c3")
    p = producer()
