#!/usr/bin/env python3
#


from threading import Thread, Event
import threading
import time, random


def conn_mysql():
    count = 1
    while not event.is_set():
        if count >= 4:
            raise TimeoutError('time out')
        print(f'{threading.current_thread().getName()}第{count}次尝试连接')
        event.wait(1)
        count += 1
    print(f'\n{threading.current_thread().getName()}连接成功\n')


def check_mysql():
    print(f'\033[45m{threading.current_thread().getName()}正在检查mysql\033[0m')
    # check时间可能为1、2、3、4、5、6，其中1、2、3连接成功，4，5，6连接失败，成败概率各为 50%
    check_duration = random.randint(1, 6)
    print(f'sleep: {check_duration}')
    time.sleep(check_duration)
    event.set()


if __name__ == '__main__':
    event = Event()
    conn1 = Thread(target=conn_mysql)
    conn2 = Thread(target=conn_mysql)
    check = Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()
