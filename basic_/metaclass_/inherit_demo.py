#!/usr/bin/env python3
#

def ma(cls):
    print('mothod a')


def mb(cls):
    print('mothod b')


method_dict = {
    'ma': ma,
    'mb': mb
}


class DynamicMethod(type):

    def __new__(cls, name, bases, attrs):
        # __new__(cls, name, bases, attrs)
        #
        # cls: 将要创建的类，类似与self，但是self指向的是instance，而这里cls指向的是class
        # name: 类的名字，也就是我们通常用类名.__name__获取的。
        # bases: 基类
        # attrs: 属性的dict。dict的内容可以是变量(类属性），也可以是函数（类方法）。

        if name[:3] == 'Abc':
            attrs.update(method_dict)
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, dct):
        super(DynamicMethod, cls).__init__(name, bases, dct)


class AbcTest(object, metaclass=DynamicMethod):
    # __metaclass__ = DynamicMethod

    def mc(self, x):
        print(x * 3)


class NotAbc(object, metaclass=DynamicMethod):
    # __metaclass__ = DynamicMethod

    def md(self, x):
        print(x * 3)


def main():
    a = AbcTest()
    a.mc(3)
    # a.ma()
    print('\ndir a: {}'.format(dir(a)))

    b = NotAbc()
    print('\ndir b: {}'.format(dir(b)))

    print('\ndiff dir(a) to dir(b): {}'.format(set(dir(a)) - set(dir(b))))


if __name__ == '__main__':
    main()
