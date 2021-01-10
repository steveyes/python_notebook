#!/usr/bin/env python3
#

import os
import sys
import time
from functools import wraps
from math import sqrt

debug_log = sys.stdout
debug_err = sys.stderr


def trace(hint):
    def decorator(func):
        @wraps(func)
        def wraper(*args, **kwargs):
            debug_log.write(
                f'\nPid: {os.getpid():d} running {hint:s} [function: {func.__name__:s}()] at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()):s}\n')
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                debug_log.write(f'Return error: {e}\n')
                return False
            debug_log.write(f'Return value: {res}\n')
            return res

        return wraper

    return decorator


@trace('calc the square')
def square(x):
    """Calculate the square of the given number."""
    return x * x


@trace('calc the sqrt')
def square_root(x):
    """Calculate the squrt of the given number."""
    return sqrt(x)


if __name__ == '__main__':
    print(square(3))
    square_root(9)
    square_root(-9)
