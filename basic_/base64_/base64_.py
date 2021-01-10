#!/usr/bin/env python3
#


import base64
from binascii import a2b_base64, b2a_base64

_copyright = 'CKW2019'


def demo01():
    # to bs
    cpr_bs = _copyright.encode(encoding='utf-8')
    print(f"copyright bytes: {cpr_bs}")

    # b64encode
    cpr_b64 = base64.b64encode(cpr_bs)
    print(f"copyright b64encoded bytes: {cpr_b64}")
    print(f"copyright b64encoded string: {cpr_b64.decode()}")

    # b64decode
    cpr_de = base64.b64decode(cpr_b64)
    print(f"copyright b64decoded bytes: {cpr_de}")
    print(f"copyright b64decoded string: {cpr_de.decode()}")


def demo02():
    # to bytes
    cpr_bs = _copyright.encode(encoding='utf-8')
    print(f"copyright bytes: {cpr_bs}")

    # b64encode
    cpr_b64 = b2a_base64(cpr_bs)
    print(f"copyright b64encoded bytes: {cpr_b64}")
    print(f"copyright b64encoded string: {cpr_b64.decode()}")

    # b64decode
    cpr_de = a2b_base64(cpr_b64)
    print(f"copyright b64decoded bytes: {cpr_de}")
    print(f"copyright b64decoded string: {cpr_de.decode()}")


if __name__ == '__main__':
    # raw string
    print(f"copyright raw string: {_copyright}")
    print(f"{'-' * 79}")
    demo01()
    print(f"{'-' * 79}")
    demo02()
