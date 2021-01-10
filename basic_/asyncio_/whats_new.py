#!/usr/bin/env python3
#

import threading
import asyncio

'''
@asyncio.coroutine: This decorator is deprecated and is scheduled for removal in Python 3.10.

This decorator should not be used for async def coroutines.
'''

class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


@asyncio.coroutine
def hello():
    print('hello world! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('hello again (%s)' % threading.current_thread())


def hello_event():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    reader, writer = yield from connect
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


def wget_event():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    hello_event()
    # wget_event()
