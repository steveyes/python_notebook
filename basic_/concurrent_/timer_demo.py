#!/usr/bin/env python3
#
#


from threading import Timer


def hello():
    print('hello, workd')


t = Timer(3, hello)

t.start()  # 3秒后执行
