#!/usr/bin/env python3
#


# 多线程并发方式一:
import threading
import time


def kantu():
    print("看图")
    time.sleep(2)
    print("看图结束")


def tingge():
    print("看图")
    time.sleep(5)
    print("看图结束")
    print(time.time() - s)  # 计算整个程序运行时间，不能放在函数外，因为函数外是主线程，此时主线程已执行完毕，等待非daemon的线程全部退出。


s = time.time()
t1 = threading.Thread(target=kantu)  # 创建看图线程,多线程的主进程.
t2 = threading.Thread(target=tingge)  # 创建听歌线程,多线程的主进程
t1.start()  # 运行看图线程,多线程的子线程
t2.start()  # 运行听歌线程,多线程的子进程
print("ending")  # 多线程的主进程
