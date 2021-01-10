#!/usr/bin/env python3
#


def myfunc(a, b):
    return a + b


funcs = [myfunc]

if __name__ == '__main__':
    print(funcs[0](2, 3))
