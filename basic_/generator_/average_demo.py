#!/usr/bin/env python3
#

from functools import wraps
from collections import namedtuple

'''
子生成器产出的值都直接传给委派生成器的调用方（客户端代码）

使用send() 方法发给委派生成器的值都直接传给子生成器。
如果发送的值是None，那么会调用子生成器的 __next__()方法。
如果发送的值不是None，那么会调用子生成器的send()方法。
如果调用的方法抛出StopIteration异常，那么委派生成器恢复运行。任何其他异常都会向上冒泡，传给委派生成器。

生成器退出时，生成器（或子生成器）中的return expr 表达式会触发 StopIteration(expr) 异常抛出。

yield from表达式的值是子生成器终止时传给StopIteration异常的第一个参数。

传入委派生成器的异常，除了 GeneratorExit 之外都传给子生成器的throw()方法。
如果调用throw()方法时抛出 StopIteration 异常，委派生成器恢复运行。
StopIteration之外的异常会向上冒泡。传给委派生成器。

如果把 GeneratorExit 异常传入委派生成器，或者在委派生成器上调用close() 方法，那么在子生成器上调用close() 方法，如果他有的话。
如果调用close() 方法导致异常抛出，那么异常会向上冒泡，传给委派生成器；否则，委派生成器抛出 GeneratorExit 异常。
'''

result = namedtuple('result', 'count average')


def coroutine(func):
    # 调用 average_gen.send(x)之前，一定要调用next(average_gen)。为了简化协程的用法，可以使用一个预激装饰器。
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


# 子生成器
def averager():
    '''functools.wraps 可以将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,或者通过参数选择
    '''
    result = namedtuple('result', 'count average')
    total = 0.0
    count = 0
    avg = None

    while True:
        print('in average_gen, before yield')
        # 子生成器产出的值都直接传给委派生成器的调用方
        term = yield avg
        if term is None:
            '''
            如果子生成器抛出 StopIteration 异常，那么委派生成器恢复运行。
            任何其他异常都会向上冒泡，传给委派生成器；
            '''
            break
        total += term
        count += 1
        avg = total / count

    print('in average_gen, return result')
    # 返回的Result 会成为grouper函数中yield from表达式的值
    # 生成器退出时，生成器（或子生成器）中的 return expr 表达式会触发StopIteration(expr) 异常抛出
    return result(count, avg)


@coroutine
# 委派生成器
def grouper(results, key):
    # 这个循环每次都会新建一个averager 实例，每个实例都是作为协程使用的生成器对象
    while True:
        print('in grouper, before yield from everage_gen, key is: ', key)
        '''
        注意，使用yield from句法调用协程时，会自动预激。
        yield from 结果会在内部自动捕获StopIteration 异常。这种处理方式与 for 循环处理StopIteration异常的方式一样。
        对于yield from 结构来说，解释器不仅会捕获StopIteration异常，还会把value属性的值变成yield from 表达式的值。
        # yield from 的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，
        使两者可以直接发送和产出值，还可以直接传入异常，而不用在中间的协程添加异常处理的代码。
        '''
        results[key] = yield from averager()
        print('in grouper, after yield from, key is:', key)


# 调用方
def main(data):
    results = {}
    for key, values in data.items():
        # group 是调用grouper函数得到生成器
        group = grouper(results, key)
        print('\ncreate group: ', grouper)
        print('\npre active group ok')
        for value in values:
            # 把各个value传给grouper 传入的值最终到达averager函数中；
            # grouper并不知道传入的是什么，同时grouper实例在yield from处暂停
            print('send to %r value %f now' % (group, value))
            '''使用 send() 方法发给委派生成器的值都直接传给子生成器。如果发送的值是None，那么会调用子生成器的 __next__() 方法。
            如果发送的值不是 None，那么会调用子生成器的 send() 方法。

            '''
            group.send(value)
        # 把None传入groupper，传入的值最终到达averager函数中，导致当前实例终止。然后继续创建下一个实例。
        # 如果没有group.send(None)，那么averager子生成器永远不会终止，委派生成器也永远不会在此激活，也就不会为result[key]赋值
        print('send to %r none' % group)
        group.send(None)
    print('report result: ')
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg': [40, 41, 42, 43, 44, 54],
    'girls;m': [1.5, 1.6, 1.8, 1.5, 1.45, 1.6],
    'boys;kg': [50, 51, 62, 53, 54, 54],
    'boys;m': [1.6, 1.8, 1.8, 1.7, 1.55, 1.6],
}

if __name__ == '__main__':
    print(averager.__name__)
    print(averager.__doc__)
    main(data)
