from typing import Iterator, Iterable, Optional, Mapping, MutableMapping, Sequence, List, Set
from typing_extensions import Protocol


# You can also define your own protocols.
# This is done by inheriting from Protocol and defining the function signatures (with empty function bodies) that the protocol expects.
# The following example shows how len() and Sized could have been implemented:
class Sized(Protocol):
    def __len__(self) -> int: ...


# A protocol specifies one or more methods that must be implemented.
# For example, all classes defining .__len__() fulfill the typing.Sized protocol.
# We can therefore annotate len() as follows:
def size(obj: Sized) -> int:
    return obj.__len__()


class IntList:
    def __init__(self, value: int, next: Optional['IntList']) -> None:
        self.value = value
        self.next = next

    def __iter__(self) -> Iterator[int]:
        current = self
        while current:
            yield current.value
            current = current.next


def print_numbered(items: Iterable[int]) -> None:
    for n, x in enumerate(items):
        print(n + 1, x)


x = IntList(3, IntList(4, IntList(5, None)))
print_numbered(x)
print_numbered([4, 5, 6, 7])


# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def f(ints: Iterable[int]) -> List[str]:
    return [str(x) for x in ints]


f(range(1, 3))


# Mapping describes a dict-like object (with "__getitem__") that we won't mutate
def m(my_dict: Mapping[int, str]) -> List[int]:
    # error hint here
    my_dict[5] = 'maybe'
    return list(my_dict.keys())


print(m({3: 'yes', 4: 'no'}))


# and MutableMapping one (with "__setitem__") that we might
def m(my_mapping: MutableMapping[int, str]) -> Set[str]:
    my_mapping[5] = 'maybe'
    return set(my_mapping.values())


print(m({3: 'yes', 4: 'no'}))
