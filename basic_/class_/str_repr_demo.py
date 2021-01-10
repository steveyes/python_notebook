#!/usr/bin/env python3
#


class Person(object):

    def __init__(self, name="", age=0) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return 'Person(name=' + self.name + ', age=' + str(self.age) + ')'


class PersonV1(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return {'name': self.name, 'age': self.age}


class PersonV2(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return '{name:' + self.name + ', age:' + str(self.age) + '}'


def print_str(p: PersonV1):
    print("<in printStr>")
    print(p)
    print(p.__str__())
    print(type(p.__str__()))
    print(str(p))
    print()


def print_repr_v1(p: PersonV1):
    print("<in printReprV1>")
    print(p.__repr__())
    print(type(p.__repr__()))
    try:
        print(repr(p))
    except:
        print("non-printable")
    print()


def print_repr_v2(p: PersonV2):
    print("<in printReprV2>")
    print(p.__repr__())
    print(type(p.__repr__()))
    print(repr(p))
    print()


if __name__ == '__main__':
    p1 = PersonV1('Pankaj', 34)
    print_str(p1)
    print_repr_v1(p1)
    p2 = PersonV2('Pankaj', 34)
    print_repr_v2(p2)
