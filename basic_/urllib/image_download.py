#!/usr/bin/env python3
#


from urllib import request


def main():
    url = 'http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLKHSVpzcqpIZwq9uTWiaVfhFMB6yUhCic3TAPg4PfZYjpV5QeyP8htQcLRicq5tee1XePozf6k60nZg/132'
    res = request.urlopen(url).read()
    with open('./info.jpg', 'wb') as ff:
        ff.write(res)


if __name__ == '__main__':
    main()
