#!/usr/bin/env python3
#


def process_data(a, b, c, d):
    print(a, b, c, d)


if __name__ == '__main__':
    x = {'a': 1, 'b': 2}
    y = {'c': 3, 'd': 4}

    process_data(**x, **y)
    process_data(**x, c=3, d=4)
    process_data(a=1, b=2, **y)
