#!/usr/bin/env python3
#


import threading
import time


def run(n):
    semaphore.acquire()
    print(f"{threading.current_thread().getName()} get semaphore, num: {n} ")
    time.sleep(1.5)
    semaphore.release()


if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    t_jobs = []

    for i in range(22):
        t = threading.Thread(target=run, args=(i,))
        t.start()
        t_jobs.append(t)

    for t in t_jobs:
        t.join()

    # while threading.active_count() != 1:
    #     pass
    # else:
    #
    #     print('---- all threads done ----')
    #     print(threading.active_count())

    if threading.active_count() == 1:
        print('---- all threads done ----')
