#!/usr/bin/env python3
#

import time
import asyncio

'''

我们通过async关键字定义一个协程（coroutine）,协程不能直接运行，需要将协程加入到事件循环loop中

asyncio.get_event_loop：创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并启动事件循环

'''
now = lambda: time.time()


async def do_some_work(x):
    print('waiting: ', x)


start = now()

coroutine = do_some_work(2)
print(coroutine)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('delay: ', now() - start)
