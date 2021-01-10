#!/usr/bin/env python3
#


from collections import Iterable


def isIterable(obj):
    print(isinstance(obj, Iterable))


if __name__ == '__main__':
    obj01 = 'abcde'
    isIterable(obj01)

    obj02 = [1, 2, 3]
    isIterable(obj02)

    obj03 = 123
    isIterable(obj03)
