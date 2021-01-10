#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# class: Foo define by type()
Foo = type(
    'Foooooo',
    (),
    {
        'attr': 100,
        'get_attr': lambda cls: cls.attr,
        'power': lambda cls, x: x * x
    }
)

x = Foo()
print(x.attr)
print(x.get_attr())
print(x.power(8))


# class: Foo define by class()
class Foo:
    attr = 100

    def get_attr(self):
        return self.attr

    def power(self, x):
        return x * x


x = Foo()
print(x.attr)
print(x.get_attr())
print(x.power(8))
