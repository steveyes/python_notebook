from threading import Thread, Lock
import time

mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)

        mutexB.acquire()
        print('\033[42m%s 拿到B锁\033[0m' % self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s 拿到B锁\033[0m' % self.name)
        time.sleep(2)

        mutexA.acquire()
        print('\033[44m%s 拿到A锁\033[0m' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()  # 使用start()会造成死锁
        # t.run() # 使用run()不会造成死锁, 或者使用RLOCK递归锁也不会造成死锁
