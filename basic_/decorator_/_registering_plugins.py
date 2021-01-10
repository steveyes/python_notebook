import random

PLUGINS = dict()


def register(func):
    """register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"hello {name}"


@register
def say_goodbye(name):
    return f"goodbye {name}"


def pick_funcs_randomly(name):
    g, gf = random.choice(list(PLUGINS.items()))
    print(f"using {g!r}")
    return gf(name)


print(PLUGINS)
pick_funcs_randomly("Alice")
