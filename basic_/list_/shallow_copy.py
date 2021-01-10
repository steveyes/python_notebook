#!/usr/bin/env python3
#


if __name__ == '__main__':

    # delete instance:
    lst = [1, 2, 3, 4, 5]
    print(f"{'-'*79}\n{lst}")
    del lst
    try:
        print(lst)
    except Exception as e:
        print(e)

    # clear all elements from a list:
    lst = [1, 2, 3, 4, 5]
    print(f"{'-'*79}\n{lst}")
    del lst[:]
    print(lst)

    # replace all elements of a list without creating a new list object:
    a = lst
    lst[:] = [7, 8, 9]
    print(f"{'-'*79}\n{lst}\n{a}")

    # create a (shallow) copy of a list:
    b = lst[:]
    print(f"{'-'*79}\n{lst}\n{b}\n{b is lst}")
