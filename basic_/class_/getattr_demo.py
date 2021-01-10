#!/usr/bin/env python3
#
from typing import Any


class bird(object):
    feather = True


class chicken(bird):
    """
    可以使用__getattr__(self, name)来查询即时生成的属性. 如果通过__dict__无法找到该属性,
    那么python会调用对象的__getattr__方法, 来即时生成该属性.
    """
    fly = False

    def __init__(self, age) -> None:
        self.age = age

    def __getattr__(self, name: str) -> Any:
        if name == 'is_adult':
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)

    def __str__(self):
        return f"chicken's __str__"


def demo01():
    summer = chicken(2)
    print(summer.is_adult)
    summer.age = 0.5
    print(summer.is_adult)
    print(summer)
    try:
        print(summer.male)
    except AttributeError as e:
        print(f'AttributeError: {e}')


if __name__ == '__main__':
    demo01()
