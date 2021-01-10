#!/usr/bin/env python3
#

from types import FunctionType


def login_required(func):
    print('login check logic here')
    return func


class LoginDecorator(type):
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if name not in ('__metaclass__', '__init__', '__module__') and type(value) == FunctionType:
                value = login_required(value)
            attrs[name] = value

        return type.__new__(cls, name, bases, attrs)


class Operation(object, metaclass=LoginDecorator):
    def login(self, x):
        print('login %s' % x)

    def delete(self, x):
        print('deleted %s' % str(x))


def main():
    op = Operation()
    op.login('alice')
    op.delete('test')


if __name__ == '__main__':
    main()
