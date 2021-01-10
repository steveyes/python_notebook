#!/usr/bin/env python3
#


"""
汉诺塔

方法参数: src, tmp, dst

分两种情况:
1 只有1个盘子
    直接从src移至dst, move(src, dst)
2 有1个以上的盘子
    1 把n-1ge盘子从起始柱移至临时柱, hano(n-1, src, dst, tmp)
    2 把第n个移至目的柱, move(src, dst)
    3 把n-1ge盘子从临时柱移至目的柱, hano(n-1, tmp, src, dst)
"""

STACK = ('A', 'B', 'C',)


def move(a, b):
    print(f"{a} -> {b}")


def hano(n, src, tmp, dst):
    if n == 1:
        move(src, dst)
    else:
        print(f"\nthe top {n} start") if n == 3 else print(f"the top {n} start")
        hano(n - 1, src, dst, tmp)
        move(src, dst)
        hano(n - 1, tmp, src, dst)
        print(f"the top {n} end\n") if n == 3 else print(f"the top {n} end")


def start_hano(i):
    hano(i, *STACK)


if __name__ == '__main__':
    start_hano(8)
