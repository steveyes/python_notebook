def decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        value = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return value

    return wrapper


@decorator
def say_hi(_name):
    return f"{_name}"


name = say_hi('world')
print(f"returning : {name}")
