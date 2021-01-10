#!/usr/bin/env python3
#

import feedparser


def url_parse(url='http://blog.csdn.net/together_cz/article'):
    feed = feedparser.parse(url)
    print(feed.keys())
    print('-----' * 20)
    print('content: {}'.format(feed['feed']['meta']['content']))
    print('name: {}'.format(feed['feed']['meta']['name']))
    print(f"entries: {feed['entries']}")
    print(f"headers: {feed['headers']}")
    print(f"href: {feed['href']}")
    print(f"status: {feed['status']}")
    print(f"encoding: {feed['encoding']}")
    print(f"version: {feed['version']}")


if __name__ == '__main__':
    url = 'http://www.163.com'
    try:
        url_parse(url)
    except Exception as e:
        print('Oops, something wrong happened!', e)
