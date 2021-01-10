#!/usr/bin/env python3
#


import threading, time


class MyThread(threading.Thread):
    def __init__(self, n, sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print('running task: ', self.n)
        time.sleep(self.sleep_time)
        print('task done: ', self.n)


if __name__ == '__main__':
    t1 = MyThread('t1', 2)
    t2 = MyThread('t2', 4)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main thread_demo....")
