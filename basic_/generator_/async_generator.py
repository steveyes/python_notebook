#!/usr/bin/env python3
#

# import from sys
import asyncio


# import from dist


# import from chekawa


# configs


# constants


# variables


# functions


# instances


async def yield_files(delay, to):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


async def get_files():
    async for i in yield_files(0.5, 10):
        print(i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(get_files())
    finally:
        loop.close()
