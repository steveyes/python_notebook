#!/usr/bin/env python3
#


import functools


def hint(pre=''):
    def decorator(_func):
        @functools.wraps(_func)
        def wrapper(*args, **kwargs):
            print(f"{pre} input {args if args else ''} {kwargs if kwargs else ''}")
            return _func(*args, **kwargs)

        return wrapper

    return decorator


@hint('^_^')
def square_sum(a, b):
    return a ** 2 + b ** 2


@hint('T_T')
def square_diff(a, b):
    return a ** 2 - b ** 2


if __name__ == '__main__':
    print(square_sum(3, 4))
    print(square_diff(5, 4))
