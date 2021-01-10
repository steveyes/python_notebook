from typing import Optional

# initialize a variable with None
oo: Optional[str] = None

# Optional[...] is a shorthand notation for Union[..., None]
# Whenever you have a keyword argument with default value None, you should use Optional.

def test_a(a: Optional[dict] = None) -> None:
    print(a)


def test_b(b: Optional[list] = None) -> None:
    print(b)


test_a()
test_a({'a1': 123, 'a2': 456})

test_b()
test_b([1, 2, 3])

"""\
Note that there is technically no difference between using Optional[] on a Union[], or just adding None to the 
Union[]. So the two sides of the following are exactly the same thing. 
Optional[Union[str, int]] <==> Union[str, int, None]
"""
