import functools


class Singleton(type):
    """Make a class a Singleton class (only one instance)
    by defining like:

        class ClassA(object, metaclass=Singleton.Singleton):
            pass

    to make it singleton
    """
    instances = dict()

    def __call__(cls, *args, **kwds):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.instances[cls]


def singleton(cls):
    """Make a class a Singleton class (only one instance)
    by defining like:

        @singleton
        class ClassA():
            pass

    to make it singleton
    """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


if __name__ == '__main__':
    class ClassOne(object, metaclass=Singleton):
        pass


    @singleton
    class ClassTwo(object):
        pass


    co1 = ClassOne()
    co2 = ClassOne()
    print(id(co1))
    print(id(co2))
    print(co1 is co2)

    ct1 = ClassTwo()
    ct2 = ClassTwo()
    print(id(ct1))
    print(id(ct2))
    print(ct1 is ct2)
