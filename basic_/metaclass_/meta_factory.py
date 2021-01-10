#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass


class Bar(metaclass=Meta):
    pass


class Qux(metaclass=Meta):
    pass


print(Foo.attr)
print(Bar.attr)
print(Qux.attr)


def MetaModel(**kwattrs):
    return type('MetaModel', (object, ), {**kwattrs})

Foo1 = MetaModel(foo=1,bar=2,qux=lambda cls, x: x * x)
x1 = Foo1()
print(x1.foo)
print(x1.bar)
print(x1.qux(8))