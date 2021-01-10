# choose.py

import random
from typing import Sequence, TypeVar

Choosable = TypeVar("Choosable", str, float)

def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

reveal_type(choose(['Guido', 'Jukka', 'Ivan']))
reveal_type(choose([1, 2, 3]))
reveal_type(choose([True, 42, 3.14]))
reveal_type(choose(['Python', 3, 7]))

# Choosable can only be either str or float, and Mypy will note that the last example is an error:
# mypy choose.py

# Also note that in the second example the type is considered float even though the input list only contains int objects.
# This is because Choosable was restricted to strings and floats and int is a subtype of float.