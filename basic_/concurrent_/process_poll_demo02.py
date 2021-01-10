#!/usr/bin/env python3
#


from multiprocessing import Process, Pool, freeze_support
import time
import os


def foo(i):
    time.sleep(1)
    print(f"in foo: {os.getpid()} --> start")
    return i ** i


def bar(arg):
    print(f"in bar: {os.getpid()} --> callback done, value: {arg}")


if __name__ == '__main__':
    pool = Pool(processes=3)  # 允许进程池同时放入3个进程
    print('in main', os.getpid())

    for i in range(10):
        # 多进程调用Foo，bar作为回调
        pool.apply_async(func=foo, args=(i,), callback=bar)
    print('main end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()
    print('all end')
