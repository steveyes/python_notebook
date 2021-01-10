#!/usr/bin/env python3
#


# 对于简单的迭代器，yield from iterable本质上等于for item in iterable: yield item的缩写版
def g(x):
    yield from range(x, 0, -1)
    yield from range(x)


def g_run(n):
    [print(gg) for gg in g(n)]


def fib(count):
    n, a, b = 0, 0, 1
    while n < count:
        # yield as generator
        yield b
        a, b = b, a + b
        n = n + 1
    return None


def fib_run(count):
    print('type of fib_iter: %s' % type(fib(5)))
    n = fib(count)
    print('type of n: %s' % type(n))
    arr_fib = []
    for nn in n:
        arr_fib.append(nn)
    # print('type of fib_run: %s' % type(fib_run(5)))
    return arr_fib


if __name__ == '__main__':
    arr_fib = fib_run(10)
    print(arr_fib)
