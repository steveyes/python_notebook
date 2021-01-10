import functools
import math


def debug(func):
    """print the function signature and return value"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature}): ")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned: {value!r}")
        print()
        return value

    return wrapper


@debug
def greeting(name, first_time=False):
    if first_time:
        return f"Hi {name}, nice to meet you!"
    else:
        return f"Hi {name}, long time no see, how are you!"


if __name__ == '__main__':
    greeting('alice')
    greeting('alice', first_time=True)

    # factorial = debug(lambda n: math.factorial(n))
    factorial = debug(math.factorial)


    def approximate_e(terms=18):
        return sum(1 / factorial(n) for n in range(terms))


    print(approximate_e(5))
    print(approximate_e(10))
