#!/usr/bin/env python3
#

class demo01():
    '''
    yield: 实现生成器，将函数变成了一个类似于迭代器的对象，可以使用for循环取值。
    '''

    @staticmethod
    def get_func():
        yield 1
        yield 2
        yield 3

    @staticmethod
    def main():
        gen = demo01.get_func()
        for i in range(3):
            # 此处不能用send，会报错TypeError: can't send non-None value to a just-started generator
            # 除非和 demo02中一样，在 for循环之前先调用一下 gen.send(None)
            # print(gen.send(i))
            print(next(gen))


class demo02():
    '''
    yield send: send有着next差不多的功能，不过send在传递一个值给生成器的同时，还能获取到生成器yield抛出的值。
    '''

    @staticmethod
    def get_func():
        a = yield 1
        print('a: ', a)

        b = yield 2
        print('b: ', b)

        c = yield 3
        print('c: ', c)

        return 'finish'

    @staticmethod
    def main():
        gen = demo02.get_func()
        gen.send(None)
        for i in range(3):
            try:
                print(gen.send(i))
            except StopIteration as e:
                print('e: ', e)


class demo03():
    '''
    yield from:
    '''
    @staticmethod
    def get_func():
        a = yield 1
        print('a: ', a)

        b = yield 2
        print('b: ', b)

        c = yield 3
        print('c: ', c)

        return 4

    @staticmethod
    def middle():
        gen = demo03.get_func()
        ret = yield from gen
        print('ret: ', ret)
        return 'middle Exception'

    @staticmethod
    def main():
        mid = demo03.middle()
        mid.send(None)
        for i in range(4):
            try:
                print(mid.send(i))
            except StopIteration as e:
                print('e: ', e)


if __name__ == '__main__':
    demo03.main()
