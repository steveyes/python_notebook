#!/usr/bin/env python3
#

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 和next方法一样 获取下一个值，必须先使用None参数调用一次， 执行到yield
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        # 先发送值给yield语句，再次执行到yield语句时返回
        r = c.send(n)
        print('[PRODUCER] Consumer return:%s' % r)
    c.close()


produce(consumer())
