#!/usr/bin/env python3
#


def _add(x, y):
    return x + y


def _sub(x, y):
    return x - y


def _mul(x, y):
    return x * y


def _div(x, y):
    return x / y


def _reduce(func, repo):
    total = repo[0]
    for nn in repo[1:]:
        total = func(total, nn)

    return total


if __name__ == '__main__':
    _repo = [1, 3, 5, 7, 9]
    print(_reduce(_add, _repo))
    print(_reduce(_sub, _repo))
    print(_reduce(_mul, _repo))
    print(_reduce(_div, _repo))
