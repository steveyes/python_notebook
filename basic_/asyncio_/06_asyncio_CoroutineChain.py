#!/usr/bin/env python3
#


import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


async def main():
    coroutine4 = do_some_work(4)
    coroutine2 = do_some_work(2)
    coroutine1 = do_some_work(1)

    tasks = [asyncio.ensure_future(task) for task in (coroutine4, coroutine2, coroutine1)]

    # #1: do the same as #2 and #3
    # dones, pending = await asyncio.wait(tasks)
    # for done in dones:
    #     print('task result: ', done.result())

    # #2: do the same as #1 and #3
    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print('task result: ', result)

    # #2: do the same as #1 and #2
    for task in asyncio.as_completed(tasks):
        print(f'task result: {await task}')


if __name__ == '__main__':
    start = now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('time: ', now() - start)
