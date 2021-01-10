#!/usr/bin/env python3
#

from urllib import request
from urllib import error


def url_error():
    url = "http://www.iloveyou.com"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)


def http_error():
    url = "http://www.douyu.com/123456.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
    except error.HTTPError as e:
        print(e.code)


def both_error():
    url = "http://www.douyu.com/123456.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
    # HTTPError是URLError的子类，所以必须放在前面，不然的话，HTTP异常就会被URLError捕获了
    except error.HTTPError as e:
        print("HTTPError")
        print(e.code)
    except error.URLError as e:
        print("URLError")
        print(e.reason)


if __name__ == '__main__':
    both_error()
