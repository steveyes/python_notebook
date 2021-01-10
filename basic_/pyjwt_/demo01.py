#!/usr/bin/env python3
#

# pip install pyjwt
import jwt
import time


def main():
    phone = '12332101278'
    uid = '1278'
    payload = {
        "iss": "www.chekawa.com",
        "iat": int(time.time()),
        "exp": int(time.time() + 86400 * 7),
        "phone": phone,
        "uid": uid,
    }

    __secret = 'bnu1xl!;PvNhUm<3Mnq0'
    __algorithm = 'HS256'
    token = (b'Bearer ' + jwt.encode(payload, __secret, algorithm=__algorithm)).decode()
    print(token)

    ttoken = token.encode().lstrip(b'Bearer').strip()
    print(ttoken)

    res = jwt.decode(ttoken, __secret, algorithm=[__algorithm, ])
    print(res)


if __name__ == '__main__':
    main()
