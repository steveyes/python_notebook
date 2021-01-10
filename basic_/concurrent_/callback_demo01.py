#!/usr/bin/env python3
#


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import requests
import json
import os


def get_page(url):
    print(f'process {os.getpid()} get {url}')
    response = requests.get(url)
    if response.status_code == 200:
        return {'url': url, 'text': response.text}


def parse_page(res):
    # parse_page 作为回调函数，拿到的是get_page返回的future对象obj，需要用obj.result()拿到里面的数据
    res = res.result()
    print(f"{os.getpid()} parse {res['url']}")
    parse_res = f"url: {res['url']}, size: {len(res['text'])}\n"
    with open('db.txt', 'a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = (
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.openstack.org/',
        'https://www.github.com/',
        'http://www.sina.com.cn/'
    )

    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)
