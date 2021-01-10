#!/usr/bin/env python3
#


import queue


def demo01():
    q = queue.PriorityQueue()

    q.put((0, 'alice'))
    q.put((5, 'bob'))
    q.put((10, 'carol'))
    q.put((15, 'chuck'))

    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == '__main__':
    demo01()
