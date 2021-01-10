#!/usr/bin/env python3
#


'''委派生成器：包含 yield from <iterable> 表达式的生成器函数；

子生成器：从 yield from 表达式中 <iterable> 部分获取的生成器；

调用方：调用委派生成器的客户端代码；
'''

def yield_gen():
    for a in 'ABC':
        yield a
    for i in range(1, 4):
        yield i


def yield_from_gen():
    yield from 'ABC'
    yield from range(1, 4)


if __name__ == '__main__':
    print(list(yield_gen()))
    print(list(yield_from_gen()))
