#!/usr/bin/env python3
#


def demo01(ss):
    for i in [None] + list(range(-1, -len(ss), -1)):
        print(ss[:i])


if __name__ == '__main__':
    ss = 'abcde'
    demo01(ss)
