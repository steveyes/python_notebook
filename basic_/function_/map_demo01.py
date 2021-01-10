#!/usr/bin/env python3
#


def _map(func, seq):
    mapped_seq = []
    for ss in seq:
        mapped_seq.append(func(ss))

    return mapped_seq


def demo01():
    print(list(map(lambda x: 2 * x, [0, 1, 2, 3, 4, 5])))
    print([2 * x for x in range(6)])


def demo02():
    print(list(map(lambda x, y: x + y, [1, 3, 5, ], [2, 4, 6, ])))
    print(list(map(lambda x, y: (x + y, x - y), [1, 3, 5, ], [2, 4, 6, ])))
    print(list(zip([1, 3, 5], [2, 4, 6])))


if __name__ == '__main__':
    demo01()
    print('-' * 79)
    demo02()
