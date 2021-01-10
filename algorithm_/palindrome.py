#!/usr/bin/env python3
#


def _is_palindrome(n):
    return str(n) == str(n)[::-1]


def demo01():
    return list(filter(_is_palindrome, range(1, 1000)))


def demo02():
    return list(n for n in range(1, 1000) if int(str(n)[::-1]) == n)


if __name__ == '__main__':
    print(demo01())
    print(demo02())
