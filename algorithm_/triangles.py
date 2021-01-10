#!/usr/bin/env python3
#


def triangles():
    ll = [1]
    while True:
        yield ll
        l1 = [0] + ll[:]
        l2 = ll[:] + [0]
        ll = [l1[i] + l2[i] for i in range(len(l1))]


if __name__ == '__main__':
    n, _max = 0, 10
    for tt in triangles():
        print(tt)
        n = n + 1
        if n == _max:
            break
