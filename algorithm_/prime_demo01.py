#!/usr/bin/env python3
#

"""
埃氏筛法(埃拉托色尼)

首先，将2到n范围内的所有整数记下来，其中最小的数字2为素数。在表中将2的倍数划去，表中剩下最小的数为3，不能被更小的整除，然后将3的倍数划去。

如果表中剩下的最小数为n，n是素数，然后将表中所有n的倍数都划去。像这样反复的操作，就能依次枚举i以内的素数了。

复杂度: nloglogn

"""


# 构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


# 定义一个筛选函数, 只保留除不尽的, 可以用偏函数代替
def _indivisible(n):
    return lambda x: x % n != 0


# 定义一个生成器, 不断返回下一个素数
def primes():

    # 第一个素数: 2
    yield 2
    it = _odd_iter()

    while True:

        # 第一个素数: 3, 并以3为除数,
        n = next(it)
        yield n
        it = filter(_indivisible(n), it)


if __name__ == '__main__':
    for i in primes():
        if i < 50:
            print(i)
        else:
            break
