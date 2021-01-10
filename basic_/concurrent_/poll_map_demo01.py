#!/usr/bin/env python3
#


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print(f'{os.getpid()} is running')
    time.sleep(1)
    return n * 2


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)

    for i in range(1, 11):
        future = executor.submit(task, i)

    # map 取代了for+submit
    executor.map(task, range(1, 11))
