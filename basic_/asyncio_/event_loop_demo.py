#!/usr/bin/env python3
#

import time
import asyncio


# @asyncio.coroutine
# def slow_operation(n):
# asyncio.coroutine 修饰 def 被 async def 替代
async def slow_operation(n):
    # yield from 被 await 替代
    # yield from asyncio.sleep(1)
    await asyncio.sleep(1)
    print('Slow operation {} complete'.format(n))


@asyncio.coroutine
def main():
    start = time.time()
    yield from asyncio.wait([slow_operation(1), slow_operation(2), slow_operation(3), ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


