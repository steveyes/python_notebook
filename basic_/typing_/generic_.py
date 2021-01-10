from typing import Dict, Mapping, Sequence, TypeVar

Employee = Dict[str, str]


def notify_by_email(
        employees: Sequence[Employee],
        overrides: Mapping[str, str]
) -> None: ...


T = TypeVar('T')


def first(l: Sequence[T]) -> T:
    return l[0]



