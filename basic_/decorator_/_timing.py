import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        # Three conversion flags are currently supported:
        # '!s' which calls str() on the value,
        # '!r' which calls repr() and
        # '!a' which calls ascii().
        print(f"finished {func.__name__!r} in {run_time:.4f} secs")

        return value

    return wrapper


@timer
def some_func(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


if __name__ == '__main__':
    some_func(1000)
