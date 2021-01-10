from dataclasses import dataclass

from ._debugging import debug
from ._timing import timer


class Circle(object):
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        """.radius is a mutable property: it can be set to a different value. 
        However, by defining a setter method, we can do some error testing to make sure it’s not set to a nonsensical negative number. 
        Properties are accessed as attributes without parentheses."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError('Radius must be positive')

    @property
    def area(self):
        """Calculate area inside circle"""
        """.area is an immutable property: properties without .setter() methods can’t be changed. 
        Even though it is defined as a method, it can be retrieved as an attribute without parentheses."""
        return self.pi() * self.radius ** 2

    def cylinder_volumn(self, height):
        """Calculate volumn of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls, radius=1):
        """Factory method creating a circle with radius 1"""
        """.unit_circle() is a class method. It’s not bound to one particular instance of Circle. 
        Class methods are often used as factory methods that can create specific instances of the class."""
        return cls(radius)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        """.pi() is a static method. It’s not really dependent on the Circle class, except that it is part of its namespace. 
        Static methods can be called on either an instance or the class."""
        return 3.1415923535


class TimeWaster_v1(object):

    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


@dataclass
class PlayingDota:
    name: str
    age: int


@timer
class Timewaster_v2(object):
    """Decorating a class does not decorate its methods. Recall that @timer is just shorthand for TimeWaster = timer(TimeWaster).s"""
    """Here, @timer only measures the time it takes to instantiate the class"""

    def __init__(self, max_num) -> None:
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(num_times)])
