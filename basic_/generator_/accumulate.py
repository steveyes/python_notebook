#!/usr/bin/env python3
#

'''
同义词:
    子生成器: 迭代器
    外部生成器: 委派生成器
'''


# 子生成器产生的值直接返还给调用者，如果为None则返回累加结果，否则累加
def accumulate():
    tally = 0
    while 1:
        recv = yield
        if recv is None:
            # 一个生成器中的return expr语句将会从生成器退出并抛出 StopIteration(expr)异常
            return tally
        tally += recv


# 外部生成器，将累加操作任务委派给子生成器
def gather_tallies(tallies):
    while 1:
        # yield from允许子生成器直接从调用者接收其发送的信息，或者抛出调用时遇到的异常，并且返回给委派生成器一个值
        tally = yield from accumulate()
        tallies.append(tally)


def gat_run():
    tallies = []
    acc = gather_tallies(tallies)

    # 使累加生成器准备好接收传入值
    next(acc)

    # 任何使用send()方法发给委派生成器的值被直接传递给迭代器，如果不为None，则调用迭代器的send()方法
    # 任何使用send()方法发给委派生成器的值被直接传递给迭代器，如果为None，则调用迭代器的next()方法
    # acc.send(None) 结束累加
    for i in range(4):
        acc.send(i)
    acc.send(None)
    print(tallies)

    for i in range(5):
        acc.send(i)
    acc.send(None)
    print(tallies)


if __name__ == '__main__':
    gat_run()
