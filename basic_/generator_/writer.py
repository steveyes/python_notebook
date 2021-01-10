#!/usr/bin/env python3
#

def writer():
    # 读取send传进的数据，并模拟写进套接字或文件
    while True:
        # w 接受send传进来的数据
        w = yield
        print('>> ', w)


def writer_wrapper(coro):
    pass


w = writer()
wrap = writer_wrapper(w)
print(wrap)
# 生成器准备好接收数据
wrap.send(None)
for i in range(4):
    wrap.send(i)

