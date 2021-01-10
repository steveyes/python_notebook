#!/usr/bin/env python3
#


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random

'''
submit: 异步提交任务
shutdown(wait=True): 相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前
'''


def task(n):
    print(f'{os.getpid()} is running')
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)

    futures = []

    for i in range(11):
        future = executor.submit(task, i)
        futures.append(future)

    executor.shutdown()
    print('----- result is -----')
    for future in futures:
        print(future.result())
