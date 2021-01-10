import functools

from basic_.decorator_ import count_calls


def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper


@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@functools.lru_cache(maxsize=4)
def fib(num):
    print(f"Calculating fib({num})")
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


if __name__ == '__main__':
    print(fibonacci(10))
    # Note that in the final call to fibonacci(8), no new calculations were needed,
    # since the eighth Fibonacci number had already been calculated for fibonacci(10).
    print(fibonacci(8))

    print(fib(10))
    print(fib(8))
    print(fib(5))
    print(fib(8))
    print(fib(5))
    print(fib.cache_info())


