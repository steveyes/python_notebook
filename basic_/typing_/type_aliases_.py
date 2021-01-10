from typing import List
from typing import Dict, Tuple, Sequence

Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


def test_scale():
    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    print(new_vector)


ConnectionOptions = Dict[str, str]
Address = Tuple[str, str]
Server = Tuple[Address, ConnectionOptions]


# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...


# Note that None as a type hint is a special case and is replaced by type(None).

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_messages(
        message: str,
        servers: Sequence[Tuple[Tuple[str, str]], Dict[str, str]]
) -> None: ...






if __name__ == '__main__':
    test_scale()
