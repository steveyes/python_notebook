from abc import ABCMeta, abstractmethod
from collections import namedtuple

from basic_.math_.utils import gcd


class AdditiveMixin(metaclass=ABCMeta):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __neg__(self):
        pass

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other


class Rational(namedtuple('Rational', ['num', 'denom']), AdditiveMixin):
    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom

        factor = gcd(num, denom)

        return super().__new__(cls, num // factor, denom // factor)

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            other = self.from_int(other)

        if isinstance(other, Rational):
            new_num = self.num * other.denom + other.num * self.denom
            new_denom = self.denom * other.denom
            return Rational(new_num, new_denom)

    @staticmethod
    def from_int(number):
        number = Rational(number, 1)
        return number

    def __neg__(self):
        return Rational(-self.num, self.denom)


if __name__ == '__main__':
    xx = Rational(12, -4)
    print(xx)
