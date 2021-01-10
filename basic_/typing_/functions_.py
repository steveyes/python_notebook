from typing import Callable, Iterator, Union, Optional, List


# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)


# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2


# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


# This is how you annotate a callable (function) value
c: Callable[[int, float], float] = f


# A generator function that yields ints is secretly
# just a function that returns an iterator of ints, so that's how we annotate it

def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


# You can of course split a function annotation over multiple lines
def send_mail(
        address: Union[str, List[str]],
        cc: Optional[List[str]],
        bcc: Optional[List[str]],
        subject='',
        body: Optional[List[str]] = None
) -> bool: ...


# An argument can be declared positional-only by giving it a name
# starting with two underscores:
def quux(__x: int) -> None:
    pass


quux(3)
quux(__x=3)
