#!/usr/bin/env python3
#


def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0] + L[:]
        L2 = L[:] + [0]
        L = [L1[i] + L2[i] for i in range(len(L1))]


if __name__ == '__main__':
    _n, _max = 0, 10
    for tt in triangles():
        print(tt)
        _n = _n + 1
        if _n == _max:
            break
