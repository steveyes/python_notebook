#!/usr/bin/env python3
#


from threading import Thread, RLock
import time

mutexA = mutexB = RLock()


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s get lock A\033[0m' % self.name)

        mutexB.acquire()
        print('\033[42m%s get lock B\033[0m' % self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s get lock B\033[0m' % self.name)
        time.sleep(2)

        mutexA.acquire()
        print('\033[44m%s get lock A\033[0m' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
