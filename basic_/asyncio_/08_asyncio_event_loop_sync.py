#!/usr/bin/env python3
#


import asyncio
from threading import Thread
from queue import Queue
import time

now = lambda: time.time()


def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()


def do_sleep(x, queue: Queue, msg=""):
    time.sleep(x)
    queue.put(msg)


queue = Queue()

new_loop = asyncio.new_event_loop()

# 定义一个线程，并传入一个事件循环对象
t = Thread(target=start_loop, args=(new_loop,))
t.start()

print(time.ctime())

# 动态添加两个协程
# 这种方法，在主线程是同步的
new_loop.call_soon_threadsafe(do_sleep, 6, queue, "first ")
new_loop.call_soon_threadsafe(do_sleep, 3, queue, "second ")

while True:
    msg = queue.get()
    print("{} coroutine finished".format(msg))
    print(time.ctime())
