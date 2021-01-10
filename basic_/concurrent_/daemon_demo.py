#!/usr/bin/env python3
#


from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('alice',))
    t.setDaemon(True)  # 必须在t.start()之前设置，此处用法为setDaemon(True)，进程中是daemon=True
    t.start()

    print('主线程')
    print(t.is_alive())
