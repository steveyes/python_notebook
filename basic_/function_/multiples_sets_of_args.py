#!/usr/bin/env python3
#


def calc01(num: list) -> int:
    sum = 0
    for n in num:
        sum += n * n
    return sum


def calc02(*num) -> int:
    sum = 0
    for n in num:
        sum += n * n
    return sum


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


if __name__ == '__main__':
    print(calc01([1, 2, 3]))

    print(calc02(1, 2, 3))
    ll = (1, 2, 3)
    print(calc02(*ll))

    print(lazy_sum(*list(range(1, 11)))())
    print(lazy_sum(*list(range(1, 101)))())
