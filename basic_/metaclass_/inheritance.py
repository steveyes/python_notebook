#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class Base():
    attr = 100


class Foo(Base):
    pass


class Bar(Base):
    pass


class Qux(Base):
    pass


print(Foo.attr)
print(Bar.attr)
print(Qux.attr)
