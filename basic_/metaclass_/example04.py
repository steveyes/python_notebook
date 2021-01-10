#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(obj):
    print('attr =', obj.attr)


Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': f
    }
)

x = Foo()
print(x.attr)
x.attr_val()


def f(obj):
    print('attr =', obj.attr)


class Foo:
    attr = 100
    attr_val = f


x = Foo()
print(x.attr)
x.attr_val()
