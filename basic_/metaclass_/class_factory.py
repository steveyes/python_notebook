#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Meta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(cls)
        cls.attr = 100


class Foo(metaclass=Meta):
    pass


class Bar(metaclass=Meta):
    pass


class Qux(metaclass=Meta):
    pass


print(Foo.attr)
print(Bar.attr)
print(Qux.attr)
