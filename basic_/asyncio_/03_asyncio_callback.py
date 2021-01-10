#!/usr/bin/env python3
#


'''
绑定回调，在task执行完成的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
'''

import time
import asyncio
import functools

now = lambda: time.time()


async def do_some_work(x):
    print('waiting: ', x)
    return 'Done after {}s'.format(x)


'''
通过add_done_callback方法给task任务添加回调函数，当task（也可以说是coroutine）执行完成的时候,就会调用回调函数。
并通过参数future获取协程执行的结果。这里我们创建 的task和回调里的future对象实际上是同一个对象
what callback do is reading the task.result(), task is the subclass of Future. 
'''


# callback without argv
def callback(future: asyncio.Future):
    print('callback: ', future.result())


start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print("\ncallback without argv:")
print(task)
task.add_done_callback(callback)
print(task)
loop.run_until_complete(task)
print('time:', now() - start)


# callback with argv
def callback(argv, future: asyncio.Future):
    print('argv: {}, callback: {}'.format(argv, future.result()))


start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print("\ncallback with argv:")
print(task)
task.add_done_callback(functools.partial(callback, 123))
print(task)
loop.run_until_complete(task)
print('time:', now() - start)

loop.close()
