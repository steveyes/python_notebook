def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_hi():
    print("Hi!")


say_hi = decorator(say_hi)

say_hi()
