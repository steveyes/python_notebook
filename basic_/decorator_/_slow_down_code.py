import functools
import time


def slow_down(_func=None, *, secs=1):
    """sleep secs seconds before calling the function"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(secs)
            return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)


@slow_down(secs=0.5)
def countdown(from_number):
    if from_number < 1:
        print("lift off")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(5)
