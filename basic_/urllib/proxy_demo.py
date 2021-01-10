#!/usr/bin/env python3
#

from urllib import request


if __name__ == '__main__':
    url = 'https://www.myip.com/'
    head = {}
    head['user-agent'] = \
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    head['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    head['accept-encoding'] = 'gzip, deflate, br'
    head['accept-language'] = 'en-US,en;q=0.9'
    proxy = {'http': '121.231.168.12:6666'}
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')]
    request.install_opener(opener)
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)
