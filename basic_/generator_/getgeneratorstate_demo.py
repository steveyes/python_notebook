#!/usr/bin/env python3
#

from inspect import getgeneratorstate

'''
GEN_CREATED：等待开始执行；

GEN_RUNNING：解释器正在执行（只有在多线程应用中才能看到这个状态）；

GEN_SUSPENDED：在 yield 表达式处暂停；

GEN_CLOSED：执行结束；
'''


def getgstst(func):
    print(getgeneratorstate(func))


def coro2(a):
    print('coro2 --> Started: a=', a)
    b = yield a
    print('coro2 --> Received: b =', b)
    c = yield a + b
    print('coro2 --> Received: c =', c)
    d = yield a + b + c
    print('coro2 --> Received: d =', d)


def coro2_wrapper():
    wrapper = coro2(14)
    list_meta = [None, 28, 42]

    for i in list_meta:
        getgstst(wrapper)
        print()
        print("round: %s" % (list_meta.index(i) + 1))
        res = wrapper.send(i)
        print('wrapper --> recv: ', res)

    try:
        wrapper.send(42)
    except StopIteration as e:
        print('error: StopIteration')
    finally:
        getgstst(wrapper)


if __name__ == '__main__':
    coro2_wrapper()
