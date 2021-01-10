#!/usr/bin/env python3
#


from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()


def crawler(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s' % (len(data), url))


def sync_crawler():
    time_start = time.time()
    for url in urls:
        crawler(url)
    print("同步cost:", time.time() - time_start)


def async_crawler():
    time_start = time.time()
    [gevent.joinall([gevent.spawn(crawler, url)]) for url in urls]
    print("异步cost:", time.time() - time_start)


if __name__ == '__main__':
    urls = ['https://www.python.org/',
            'https://www.yahoo.com/',
            'https://github.com/', ]

    sync_crawler()
    print()
    async_crawler()
