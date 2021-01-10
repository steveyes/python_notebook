#!/usr/bin/env python3
#

import chardet
import json
from urllib import request
from urllib import parse
from urllib import error


def youdao_translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

    from_data = {}
    from_data['i'] = word
    from_data['from'] = 'AUTO'
    from_data['to'] = 'AUTO'
    from_data['smartresult'] = 'dict'
    from_data['client'] = 'fanyideskweb'
    from_data['doctype'] = 'json'
    from_data['version'] = '2.1'
    from_data['keyfrom'] = 'fanyi.web'
    from_data['action'] = 'FY_BY_REALTIME'
    from_data['typoResult'] = 'false'
    data = parse.urlencode(from_data).encode('utf-8')

    req = request.Request(url, data=data, headers=head)

    json_str = None

    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
    except error.URLError as e:
        print(e.reason)
        exit()
    else:
        json_str = json.loads(html)

    res = json_str
    src = res['translateResult'][0][0]['src']
    tgt = res['translateResult'][0][0]['tgt']
    print('source lang: ', src)
    print('destination lang: ', tgt)


def main():
    word = input('please input_demo the origin word:')
    youdao_translate(word)


if __name__ == '__main__':
    main()
