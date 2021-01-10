import functools


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class TheOne:
    pass


if __name__ == '__main__':
    first_one = TheOne()
    another_one = TheOne()
    print(id(first_one))
    print(id(another_one))
    print(first_one is another_one)
