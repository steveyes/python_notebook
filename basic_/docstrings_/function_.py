from pydoc import render_doc


def say_hello(name: str) -> None:
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")


# get function signatures and docstrings
print(render_doc(say_hello))

# get docstrings
print(say_hello.__doc__)
