#!/usr/bin/env python3
#


import asyncio
import time
from threading import Thread
from queue import Queue

now = lambda: time.time()


def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x, queue: Queue, msg=""):
    await asyncio.sleep(x)
    queue.put(msg)


queue = Queue()

new_loop = asyncio.new_event_loop()

start = now()

# 定义一个线程，并传入一个事件循环对象
t = Thread(target=start_loop, args=(new_loop,))
t.start()

print(time.ctime())

# 动态添加两个协程
# 这种方法，在主线程是异步的
asyncio.run_coroutine_threadsafe(do_some_work(6, queue, "first "), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(3, queue, "second "), new_loop)

while True:
    msg = queue.get()
    print("{} coroutine finished".format(msg))
    print(time.ctime())
