#!/usr/bin/env python3
#


class MyClass: pass


obj = MyClass()


def myFunc(): pass


if __name__ == '__main__':
    print(obj.__class__.__name__)
    print(myFunc.__name__)
