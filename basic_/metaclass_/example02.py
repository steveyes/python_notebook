#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from example01 import Foo

# Here, <bases> is a tuple with a single element Foo, specifying the parent class that Bar inherits from.
# An attribute, attr, is initially placed into the namespace dictionary:

Bar = type('Barrrrr', (Foo,), dict(attr=100))

x = Bar()
print('''\n{}'''.format('-----' * 80) * 2, "\nin example02", '''\n{}'''.format('-----' * 80) * 2, "\n")
print(x.attr)
print(x.__class__)
print(x.__class__.__name__)
print(x.__class__.__bases__)
print(x.__class__.__bases__[0].__name__)


# defines a class the usual way, with the class statement
class Bar(Foo):
    attr = 100


x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__name__)
print(x.__class__.__bases__)
print(x.__class__.__bases__[0].__name__)
