#!/usr/bin/env python3
#


class num(object):

    def __init__(self, value) -> None:
        self.value = value

    def getNeg(self):
        return self.value

    def setNeg(self, value):
        self.value = -value

    def delNeg(self):
        print("value also deleted")
        del self.value

    neg = property(getNeg, setNeg, delNeg, "I'm negative")


def demo01():
    x = num(1.1)
    print(x.neg)
    x.neg = -22
    print(x.neg)
    del x.neg
    print(num1.neg.__doc__)


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value < 0 or value > 100:
            raise ValueError('must between 0 ~ 100')
        self._score = value


def demo02():
    ss = Student()
    ss.score = 99
    print(ss.score)

    try:
        ss.score = '99'
    except Exception as e:
        print(e)
    else:
        print(ss.score)

    try:
        ss.score = -1
    except Exception as e:
        print(e)
    else:
        print(ss.score)


if __name__ == '__main__':
    demo02()
