#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# defines a class dynamically with type()
Foo = type('Foooooo', (), {})
x1 = Foo()
print(x1.__class__.__name__)
print(Foo.__name__)


# defines a class the usual way, with the class statement
class Foo: pass


x2 = Foo()
print(x2.__class__.__name__)
print(Foo.__name__)
