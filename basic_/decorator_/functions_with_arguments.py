def decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        render = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return render

    return wrapper


@decorator
def say_hi(name):
    print(f"hello {name}")
    return True


ru_ok = say_hi('world')
print(ru_ok)
