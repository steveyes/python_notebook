import math
import functools
import pint


def set_unit(unit):
    """Register a unit on a function/class"""

    def decorator_set_unit(_type):
        _type.unit = unit
        return _type

    return decorator_set_unit


def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()

    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)

        return wrapper_use_unit

    return decorator_use_unit


@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius ** 2 * height


@set_unit("cm^3")
class Volume(object):
    unit = None

    def __init__(self, radius, height) -> None:
        self.radius = radius
        self.height = height

    def __call__(self, *args, **kwargs):
        return math.pi * self.radius ** 2 * self.height


@use_unit("meter per second")
def average_speed(distance, duration):
    return distance / duration


if __name__ == '__main__':
    print(volume(3, 5))
    print(volume.unit)

    vv = Volume(3, 5)
    print(vv())
    print(vv.unit)

    bolt = average_speed(100, 9.58)
    print(bolt)
    print(bolt.to("km per hour"))
    print(bolt.to("mph").m)  # Magnitude
