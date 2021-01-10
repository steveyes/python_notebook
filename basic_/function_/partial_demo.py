#!/usr/bin/env python3
#


from operator import add, mul
from functools import partial

if __name__ == '__main__':
    add1 = partial(add, 1)
    mul100 = partial(mul, 100)
    print(add1(4))
    print(add1(9))
    print(mul100(4))
    print(mul100(9))

    print(int('10010', base=2))
    base2 = partial(int, base=2)
    base2.__doc__ = 'convert base 2 string to an int'
    print(base2('10010'))

