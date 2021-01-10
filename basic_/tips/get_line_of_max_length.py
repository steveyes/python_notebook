#!/usr/bin/env python3
#

from textwrap import dedent

FF = './motd'

with open(FF, 'w+') as ff:
    ff.write(dedent('''\
    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.
    
    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    '''))

"""
生成式: []
生成器: ()
"""


def demo01():
    """
    *deprecated*
    *bug exists*: 文中含有换行会导致错误
    :return:
    """
    with open(FF, 'r') as _ff:
        max_len = 0
        while True:
            line_len = len(_ff.readline().strip())
            if not line_len:
                break
            if line_len > max_len:
                max_len = line_len

    return max_len


def demo02():
    """
    一次读取全部行, 并释放句柄
    :return:
    """
    with open(FF, 'r') as _ff:
        max_len = 0
        lines = _ff.readlines()

    for line in lines:
        line_len = len(line.strip())
        if line_len > max_len:
            max_len = line_len

    return max_len


def demo03():
    """
    全部读取到生成器中, 取得最长行后, 释放句柄
    :return:
    """
    _ff = open(FF, 'r')
    max_len = 0
    lines = (ll.strip() for ll in _ff)

    for line in lines:
        line_len = len(line.strip())
        if line_len > max_len:
            max_len = line_len

    _ff.close()

    return max_len


def demo04():
    """
    仅读取全部行的长度到生成式中, 释放句柄, 返回最大值
    :return:
    """
    _ff = open(FF, 'r')
    lens = [len(xx.strip()) for xx in _ff]
    _ff.close()
    return max(lens)


def demo05():
    """
    demo04中的生成式换成生成器, 并对其做 max() 处理
    :return:
    """
    _ff = open(FF, 'r')
    max_len = max(len(x.strip()) for x in _ff)
    _ff.close()
    return max_len


def demo06():
    with open(FF, 'r') as _ff:
        return max(len(xx.strip()) for xx in _ff)


if __name__ == '__main__':
    print(demo01())
    print(demo02())
    print(demo03())
    print(demo04())
    print(demo05())
    print(demo06())
