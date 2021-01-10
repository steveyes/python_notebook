from typing import List, Set, Dict, Tuple, Optional

ii: int = 1
ff: float = 1.0
bbl: bool = True
ss: str = "test"
bbs: bytes = b"test"

# For collections, the name of the type is capitalized,
# and the name of the type inside the collection is in brackets
l: List[int] = list()
L: List[int] = [1]

s: Set[int] = set()
S: Set[int] = {6, 7}

# same as above, but with type comment syntax
LL = [1]  # type: List[int]

# For mappings, we need the types of both keys and values
d: Dict[str, float] = dict()
D: Dict[str, float] = {'field': 2.0}

# For tuples, we specify the types of all the elements
T: Tuple[int, str, float] = (3, 'yes', 7.5)

# Use Optional[] for values that could be None
over = 'None'
o: Optional[str] = None or over

if o is not None:
    print(o.upper())

assert o is not None
print(o.upper())
