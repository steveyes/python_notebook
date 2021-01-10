#!/usr/bin/env python3
#

from typing import Any
import inspect


def get_sign(func):
    print(inspect.signature(func))


def has_attr(obj, attr):
    print(hasattr(obj, attr))


def get_class(obj: object) -> Any:
    print(obj.__class__.__bases__)
    print(obj.__class__)
    print(obj.__class__.__name__)


if __name__ == '__main__':
    def func01(a, b):
        return a ** 2 + b ** 2


    get_sign(func01)

    aa = [1, 2, 3]
    has_attr(aa, 'append')
    has_attr(func01, '__call__')

    get_class(aa)
