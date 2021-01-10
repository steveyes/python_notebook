import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return func(*args, **kwargs)

    return wrapper


@decorator
def say_hi(_name):
    return f"{_name}"


name = say_hi('world')
print(f"returning : {name}")
print(say_hi)
print(say_hi.__name__)
print(help(say_hi))
