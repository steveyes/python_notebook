#!/usr/bin/env python3
#


import threading
import time

lock = threading.Lock()

num = 0

t_objs = []


def run(n):
    lock.acquire()
    global num
    num += 1
    print(f"current num: {n}, thread: {threading.current_thread()}")
    time.sleep(1)
    lock.release()


for i in range(10):
    t = threading.Thread(target=run, args=(f"t-{i}",))
    t.start()
    t_objs.append(t)

# 等待所有子线程结束，再会到主线程
for t in t_objs:
    t.join()

print("----------all threads has finished----------")
print(f"{threading.current_thread(), threading.active_count()}")
print(f"num: {num}")
