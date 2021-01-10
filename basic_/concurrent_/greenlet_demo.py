#!/usr/bin/env python3
#


from greenlet import greenlet
import time

'''
greenlet只是提供了一种比generator更加便捷的切换方式，
当切到一个任务执行时如果遇到io，那就原地阻塞，
仍然是没有解决遇到IO自动切换来提升效率的问题。

单线程里的这20个任务的代码通常会既有计算操作又有IO操作，
我们完全可以在执行任务1时遇到阻塞，
就利用阻塞的时间去执行任务2。。。。
如此，才能提高效率，这就用到了Gevent模块。
'''


def eat(name):
    print('%s eat 1' % name)
    time.sleep(1)
    g2.switch('bob')
    time.sleep(2)
    print('%s eat 2' % name)
    time.sleep(1)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


if __name__ == '__main__':
    g1 = greenlet(eat)
    g2 = greenlet(play)
    g1.switch('alice')
