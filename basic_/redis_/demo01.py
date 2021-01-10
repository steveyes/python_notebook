#!/usr/bin/env python3
#


import json
import redis
import datetime
import sys
import multiprocessing
import time
from datetime import date
from urllib import parse

QUEUE = "apply"
redisPool = redis.ConnectionPool(host='localhost', port=6379)
client = redis.Redis(connection_pool=redisPool)


def send(key, value):
    value = json.dumps(value, ensure_ascii=False)
    client.hset(QUEUE, key, value)


def send_demo():
    for k in range(10):
        gmt_create = datetime.datetime.now().strftime('%H%M%S%f')
        print(gmt_create)
        time.sleep(1)
        gmt_update = datetime.datetime.now().strftime('%H%M%S%f')
        send(gmt_create, {"category": '请求订单', "gmt_create": gmt_create, "gmt_update": gmt_update})


def get(queue, key):
    if client.hexists(queue, key):
        kv = client.hget(queue, key)
        client.hdel(queue, key)
        return json.loads(kv)


def get_demo():
    queue = QUEUE
    return get(queue, '161807993622')


if __name__ == '__main__':
    # send_demo()
    kv = get_demo()
    print(kv)
