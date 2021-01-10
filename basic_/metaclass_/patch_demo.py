#!/usr/bin/env python3
#

def monkey_patch(name, bases, attrs):
    assert len(bases) == 1
    base = bases[0]
    for name, value in attrs.items():
        if name not in ('__module__', '__init__', '__metaclass__'):
            setattr(base, name, value)
    return base


class A(object):
    def a(self):
        print('i am object A')


class PatchA(A, metaclass=monkey_patch):
    def patcha_method(self):
        print('this is a method patched for class A')


def main():
    pa = PatchA()
    pa.patcha_method()
    pa.a()
    # print('dir(a): ', dir(pa))
    # print('dir(PatchA): ', dir(PatchA))
    # print('diff dir(PatchA) between dir(a) : ', set(dir(PatchA)) - set(dir(pa)))


if __name__ == '__main__':
    main()
