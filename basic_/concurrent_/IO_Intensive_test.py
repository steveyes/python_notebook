#!/usr/bin/env python3
#

from gevent import monkey

monkey.patch_all()
import gevent
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time


def io_func():
    # 模拟io等待时间，设置3秒
    time.sleep(3)


def by_thread(count):
    start_time = time.time()
    threads = [Thread(target=io_func) for i in range(count)]
    [threads[i].start() for i in range(count)]
    [threads[i].join() for i in range(count)]
    print(f'duration by_thread: {time.time() - start_time}')


def by_thread_pool(count):
    start_time = time.time()

    # 线程池设置并发 50000
    with ThreadPoolExecutor(50000) as executor:
        for i in range(count):
            executor.submit(io_func)

    print(f'duration by_thread_pool: {time.time() - start_time}')


def by_coroutine(count):
    start_time = time.time()
    gevent.joinall([gevent.spawn(io_func) for i in range(count)])
    print(f'duration by_coroutine: {time.time()  - start_time}')


if __name__ == '__main__':
    count = 1000000

    by_thread(count)
    by_thread_pool(count)
    by_coroutine(count)
