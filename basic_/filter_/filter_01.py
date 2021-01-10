#!/usr/bin/env python3
#


from random import randint


def demo01():
    def odd(n):
        return n % 2

    all_nums = []
    for nn in range(9):
        all_nums.append(randint(1, 99))

    print(all_nums)
    print(list(filter(odd, all_nums)))


def demo02():
    all_nums = []
    for nn in range(9):
        all_nums.append(randint(1, 99))

    print(all_nums)
    print(list(filter(lambda n: n % 2, all_nums)))


def demo03():
    all_nums = []
    for nn in range(9):
        all_nums.append(randint(1, 99))

    print(all_nums)
    print(list(nn for nn in all_nums if nn % 2))


def demo04():
    print([nn for nn in [randint(1, 99) for ii in range(9)] if nn % 2])


if __name__ == '__main__':
    demo01()
    demo02()
    demo03()
    demo04()
