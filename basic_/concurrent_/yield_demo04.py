#!/usr/bin/env python3
#


import time


def func(n):
    for i in range(0, n):
        arg = yield i
        print('in func:', arg)


if __name__ == '__main__':

    f = func(10)

    while True:
        print('main:', next(f))
        print('in main:', f.send(100))
        time.sleep(1)
