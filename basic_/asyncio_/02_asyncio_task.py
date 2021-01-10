#!/usr/bin/env python3
#

import asyncio
import time

'''
协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象. 
task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果.
'''

now = lambda: time.time()


async def do_some_work(x):
    print('waiting: ', x)


start = now()

'''
创建task后，在task加入事件循环之前为pending状态，当完成后，状态为finished

关于上面通过loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task

关于这两个命令的官网解释： https://docs.python.org/3/library/asyncio-task.html#asyncio.ensure_future
'''

# loop.create_task
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print("\nloop.create_task: ")
print("task: ", task)
loop.run_until_complete(task)
print("task: ", task)
print(isinstance(task, asyncio.Future))
print('delay: ', now() - start)

# asyncio.ensure_future
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print("\nasyncio.ensure_future: ")
print(task)
loop.run_until_complete(task)
print(task)
print(task.result())
print(isinstance(task, asyncio.Future))
print('delay: ', now() - start)

loop.close()
