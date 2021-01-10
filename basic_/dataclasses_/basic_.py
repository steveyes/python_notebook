from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt
from basic_.common import debug


@dataclass
class Position:
    """This works exactly as if you had specified the default values in the definition of the
    .__init__() method of a regular class: """
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        # Earth radius in kilometers
        r = 6371

        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2) ** 2 +
             cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))


@debug
def create_class():
    pos = Position('Oslo', 10.8, 59.9)
    print(pos)
    print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°')


@debug
def default_value():
    pos = Position('Null Island')
    print(pos)
    pos = Position('Greenwich', lat=51.8)
    print(pos)
    pos = Position('Vancouver', -123.1, 49.3)
    print(pos)


@debug
def adding_method():
    oslo = Position('Oslo', 10.8, 59.9)
    vancouver = Position('Vancouver', -123.1, 49.3)
    print(oslo.distance_to(vancouver))


if __name__ == '__main__':
    create_class()
    default_value()
    adding_method()
