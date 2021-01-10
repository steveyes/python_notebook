import functools


def repeat(_func=None, *, repeat_times=2):
    """when a decorator uses arguments, you need to add an extra outer function"""
    """Since the function to decorate is only passed in directly if the decorator is called without arguments, 
    the function m_funcust be an optional argument. This means that the decorator arguments must all be specified by keyword. 
    You can enforce this with the special * syntax, which means that all following parameters are keyword-only:"""

    @functools.wraps(_func)
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeat_times):
                print(f"Something is happening before the function is called, round: {i + 1}/{repeat_times}.")
                render = func(*args, **kwargs)
                print("after func run")
                return render

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)


@repeat(repeat_times=3)
def say_hi(name):
    print(f"hello {name}")
    return True


@repeat
def say_bye(name):
    print(f"bye {name}")
    return False


ru_ok = say_hi('world')
print(ru_ok)
ru_ok = say_bye('world')
print(ru_ok)
