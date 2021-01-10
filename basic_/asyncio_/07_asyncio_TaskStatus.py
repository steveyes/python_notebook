#!/usr/bin/env python3
#

import asyncio
import time

'''
uture对象有几个状态：

- Pending： 创建future，还未执行
- Running： 事件循环正在调用执行任务
- Done： 任务执行完毕
- Cancelled： Task被取消后的状态

创建future的时候，task为pending，
事件循环调用执行的时候当然就是running，
调用完毕自然就是done，
如果需要停止事件循环，就需要先把task取消。
可以使用asyncio.Task获取事件循环的task
'''

now = lambda: time.time()


async def do_some_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


async def main():
    coroutine10 = do_some_work(10)
    coroutine5 = do_some_work(5)
    coroutine3 = do_some_work(3)
    coroutine1 = do_some_work(1)

    tasks = [
        asyncio.ensure_future(coroutine10),
        asyncio.ensure_future(coroutine5),
        asyncio.ensure_future(coroutine3),
        asyncio.ensure_future(coroutine1)
    ]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':

    start = now()

    loop = asyncio.get_event_loop()

    # 启动事件循环之后，马上ctrl+c，会触发 run_until_complete 的执行异常 KeyBorardInterrupt。然后通过循环 asyncio.Task 取消 future
    try:
        # main() 相当于一个打包好的 asyncio.wait(tasks) 或者 asyncio.gather(*tasks)
        loop.run_until_complete(main())
    except KeyboardInterrupt as e:
        # print(asyncio.Task.all_tasks())
        [print(task) for task in asyncio.Task.all_tasks()]
        # True表示cannel成功，loop stop之后还需要再次开启事件循环，最后在close，不然还会抛出异常

        # True表示cannel成功，loop stop之后还需要再次开启事件循环，最后再close，不然还会抛出异常：
        # [print(task.cancel()) for task in asyncio.Task.all_tasks()]
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
        loop.stop()
        loop.run_forever()
    finally:

        loop.close()

    print('time: ', now() - start)
