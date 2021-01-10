import time
import redis
import asyncio
from queue import Queue
from threading import Thread


'''
预备条件: 
1. sudo apt update && sudo apt -y install redis-server
2. redis-cli lpush queue 5 && redis-cli lpush queue 3 && redis-cli lpush queue 1
'''

def start_loop(loop: asyncio.AbstractEventLoop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_sleep(x, queue: Queue):
    await asyncio.sleep(x)
    queue.put("ok")


def get_redis():
    connection_pool = redis.ConnectionPool(host='127.0.0.1', db=0)
    return redis.Redis(connection_pool=connection_pool)


def consumer():
    while True:
        task = rconn.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_sleep(int(task), queue), new_loop)


if __name__ == '__main__':
    print(time.ctime())
    new_loop = asyncio.new_event_loop()

    # 定义一个线程， 运行一个事件循环对象， 用于实时接收新任务
    loop_thread = Thread(target=start_loop, args=(new_loop,))
    loop_thread.setDaemon(True)
    loop_thread.start()

    # 创建 redis 实例
    rconn = get_redis()

    # 创建 queue 实例
    queue = Queue()

    # 子线程：用于消费队列消息，并实时往事件对象容器中添加新任务
    consumer_thread = Thread(target=consumer)
    consumer_thread.setDaemon(True)
    consumer_thread.start()

    while True:
        msg = queue.get()
        print("coroutine finished!")
        print("current time: ", time.ctime())
