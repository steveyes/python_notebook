#!/usr/bin/env python3
#

import asyncio
import functools


def calc_deco(op, delay):
    def wrapper(func_out):
        @functools.wraps(func_out)
        async def func_in(*args, **kwargs):
            print(f'task {op}: start')
            print(f'task {op}: {args[0]} {op} {args[1]}...')
            await asyncio.sleep(delay)
            print(f'task {op}: Duration {delay}')
            return await func_out(*args, **kwargs)

        return func_in

    return wrapper


@calc_deco('+', 1.5)
async def calc_add(x, y):
    return x + y


@calc_deco('-', 1.2)
async def calc_sub(x, y):
    return x - y


@calc_deco('*', 1.0)
async def calc_mul(x, y):
    return x * y


@calc_deco('/', 0.8)
async def calc_div(x, y):
    return x / y


def retrieve_deco(op):
    def wrapper(func_out):
        @functools.wraps(func_out)
        async def func_in(*args, **kwargs):
            res = await func_out(*args, **kwargs)
            print(f'task {op}: {args[0]} {op} {args[1]} = {res}')
            print(f'task {op}: Computing finished')

        return func_in

    return wrapper


@retrieve_deco('+')
async def retrieve_add(x, y):
    return await calc_add(x, y)


@retrieve_deco('-')
async def retrieve_sub(x, y):
    return await calc_sub(x, y)


@retrieve_deco('*')
async def retrieve_mul(x, y):
    return await calc_mul(x, y)


@retrieve_deco('/')
async def retrieve_div(x, y):
    return await calc_div(x, y)


async def call_back(future):
    print('callback: ', future.result)


async def main():
    x = 10
    y = 3
    coro_add = retrieve_add(x, y)
    coro_sub = retrieve_sub(x, y)
    coro_mul = retrieve_mul(x, y)
    coro_div = retrieve_div(x, y)
    tasks = [asyncio.ensure_future(task) for task in [coro_add, coro_sub, coro_mul, coro_div, ]]
    # asyncio.gather(*tasks) 也可以使用 asyncio.wait(tasks) ,前者接收一堆task，后者接收一个task列表。
    # 关于asyncio.gather和asyncio.wait官网的说明：
    # https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
    return await asyncio.gather(*tasks)


if __name__ == '__main__':

    # 创建循环事件，
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    for result in results:
        print('task result: ', result)
    loop.close()
