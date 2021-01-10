import warnings
import functools


def deprecated(_func=None, *, new_fn=None):
    """This is a decorator which can be used to mark functions as deprecated.
    It will result in a warning being emitted when the function is used.
    using like

        @deprecated
        def old_func():
            pass
    or
        @deprecated(new_fn=new_func)
        def old_func():
            pass

    """

    def wrapper(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn("The '{}' method is deprecated, "
                          "use '{}' instead".format(func.__name__, new_fn),
                          category=DeprecationWarning,
                          stacklevel=2)

            return func(*args, **kwargs)

        return new_func

    if _func is None:
        return wrapper
    else:
        return wrapper(_func)


def some_old_function(x, y):
    return x + y


class demo_02(object):
    @deprecated(new_fn=some_old_function)
    def some_old_method(self, x, y):
        warnings.warn('deprecated', DeprecationWarning, 2)
        return x + y


if __name__ == '__main__':
    some_old_function(1, 2)
    demo_02().some_old_method(1, 2)
