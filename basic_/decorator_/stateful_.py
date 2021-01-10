import functools


def count_calls(func):
    @functools.wraps(func)
    def wrap_count_calls(*args, **kwargs):
        wrap_count_calls.num_calls += 1
        print(f"call {wrap_count_calls.num_calls} {func.__name__!r}")
        return func(*args, **kwargs)

    wrap_count_calls.num_calls = 0
    return wrap_count_calls


@count_calls
def say_hi():
    print('hi!')


class CountCalls:
    """Recall that the decorator syntax @my_decorator is just an easier way of saying func = my_decorator(func).
    Therefore, if my_decorator is a class, it needs to take func as an argument in its .__init__() method.
    Furthermore, the class needs to be callable so that it can stand in for the decorated function."""

    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        """For a class to be callable, you implement the special .__call__() method:"""
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_bye():
    print("bye")


if __name__ == '__main__':
    say_hi()
    say_hi()
    say_hi()
    say_bye()
    say_bye()
    say_bye()
