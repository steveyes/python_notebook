#!/usr/bin/env python3
#


# 在__iter__函数中将使__next__ 中的StopIteration raise的条件归零，则可以循环迭代实例。


class Squares(object):
    def __init__(self, start, stop):
        self.flag = start - 1
        self.value = self.flag
        self.stop = stop

    def __iter__(self):
        self.value = self.flag
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value


a = Squares(1, 5)
b = Squares(1, 5)

s = 0
while s <= 1000:
    for i in a:
        s += i
        print(s)
