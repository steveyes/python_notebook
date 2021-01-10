import argparse
import math


def type_demo():
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', type=int)
    parser.add_argument('bar', type=open)
    open('tmp.txt', 'a').close()
    args = parser.parse_args('2 tmp.txt'.split())
    print(args)

    parser = argparse.ArgumentParser()
    parser.add_argument('bar', type=argparse.FileType('w'))
    args = parser.parse_args(['out.txt'])
    print(args)

    # type= can take any callable that takes a single string argument and returns the converted value:
    def perfect_square(string):
        value = int(string)
        sqrt = math.sqrt(value)
        if sqrt != int(sqrt):
            msg = "%r is not a perfect square" % string
            raise argparse.ArgumentTypeError(msg)
        return value

    parser = argparse.ArgumentParser()
    parser.add_argument('foo', type=perfect_square)
    args = parser.parse_args(['9'])
    print(args)
    args = parser.parse_args(['8'])
    print(args)

    # The choices keyword argument may be more convenient for type checkers that simply check against a range of values:
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', type=int, choices=range(5, 10))
    args = parser.parse_args(['7'])
    print(args)
    args = parser.parse_args(['11'])
    print(args)
