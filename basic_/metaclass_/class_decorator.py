#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class Foo:
    pass


@decorator
class Bar:
    pass


@decorator
class Qux:
    pass


print(Foo.attr)
print(Bar.attr)
print(Qux.attr)
