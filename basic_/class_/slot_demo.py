#!/usr/bin/env python3
#


class Student(object):
    __slots__ = ['name', 'age']


class Pupil(Student):
    pass


if __name__ == '__main__':
    ss = Student()

    ss.name = 'alice'
    print(ss.name)

    ss.age = '18'
    print(ss.age)

    try:
        ss.score = '99'
    except Exception as e:
        print(e)
    else:
        print(ss.score)

    # __slot__ 对子类不起作用
    pp = Pupil()

    pp.name = 'bob'
    print(pp.name)

    pp.age = '8'
    print(pp.age)

    pp.score = '99'
    print(pp.score)
