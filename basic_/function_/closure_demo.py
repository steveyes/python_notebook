#!/usr/bin/env python3
#


def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line


if __name__ == '__main__':
    line1 = line_conf()
    print(line1.__closure__)
    print(line1.__closure__[0].cell_contents)
