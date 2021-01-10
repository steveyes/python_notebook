import warnings


def some_func():
    print("some func")
    warnings.warn('deprecated', DeprecationWarning, 2)


if __name__ == '__main__':
    some_func()
