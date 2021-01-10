#!/usr/bin/env python3
#
from demo.generator.average_demo import averager
from demo.generator.getgeneratorstate_demo import getgstst


class DemoException(Exception):
    '''Custimized Exception'''


def demo_exec_handling():
    print('--> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))


def exception_in():
    exec_coro = demo_exec_handling()
    next(exec_coro)
    exec_coro.send(11)
    exec_coro.send(12)
    exec_coro.throw(DemoException)
    getgstst(exec_coro)


def exception_out():
    exec_arg = averager()
    avg = exec_arg.send(40)
    print(avg)
    avg = exec_arg.send(50)
    print(avg)
    try:
        avg = exec_arg.send('spam')
    except TypeError as te:
        print("unsupported operand type(s)")
    else:
        print(avg)


if __name__ == '__main__':
    exception_in()
    exception_out()
