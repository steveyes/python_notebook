#!/usr/bin/env python3
#


def is_define_01(xx):
    # this is wrong
    if xx in locals().keys():
        yy = 100 if not xx else xx
    else:
        yy = 100
    return yy


def is_define_02(xx):
    # this is wrong
    if xx in dir():
        yy = 100 if not xx else xx
    else:
        yy = 100
    return yy


def is_define_03(xx):
    # this is wrong
    try:
        yy = 100 if not xx else xx
    except:
        yy = 100
    return yy


if __name__ == '__main__':
    xx = None
    del xx

    # yy = is_define_01(xx)

    # yy = is_define_02(xx)

    try:
        yy = 100 if not xx else xx
    except:
        yy = 100

    print(yy)
