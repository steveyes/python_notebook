#!/usr/bin/env python3
#


import contextlib
import os
import json


def demo01(f):
    with contextlib.suppress(FileNotFoundError):
        os.remove(f)


def demo02(f):
    try:
        os.remove(f)
    except FileNotFoundError as e:
        print(json.dumps({'e.strerror': e.strerror, 'file': f}, indent=4, sort_keys=True))


if __name__ == '__main__':
    f_tmp = 'somefile.tmp'
    demo01(f_tmp)
    demo02(f_tmp)
