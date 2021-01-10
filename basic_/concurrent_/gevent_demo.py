#!/usr/bin/env python3
#


from gevent import monkey

monkey.patch_all()

import gevent
import time


def foo(name):
    print('%s Running in foo' % name)
    time.sleep(2)
    print('%s Running in foo, Explicit context switch to foo again' % name)


def bar(name):
    print('%s Running in bar, Explicit context to bar' % name)
    time.sleep(1)
    print('%s Running in bar, Implicit context switch back to bar' % name)


def cat(name):
    print('%s Running in eat' % name)
    time.sleep(0)
    print('%s Running in eat again' % name)


gevent.joinall([
    gevent.spawn(foo, 'alice'),
    gevent.spawn(bar, 'bob'),
    gevent.spawn(cat, 'carol'),
])
