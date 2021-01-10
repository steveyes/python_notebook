from dataclasses import dataclass
from timeit import timeit
from pympler import asizeof


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital(Position):
    country: str = 'Unknown'
    lat: float = 40.0


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float


if __name__ == '__main__':
    print(Capital('Oslo', country="Norway"))
    pos = Position('London', -0.1, 51.5)
    slot = SlotPosition('Madrid', -3.7, 40.4)
    print(asizeof.asizeof(pos))
    print(asizeof.asizeof(slot))
    print(timeit('simple.name', setup="simple=Position('Oslo', 10.8, 59.9)", globals=globals()))
    print(timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals()))
