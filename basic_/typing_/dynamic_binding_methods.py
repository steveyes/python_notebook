from types import MethodType


class Student(object):
    name: str
    age: int
    score: float
    pass


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


if __name__ == '__main__':
    s = Student()

    # dynamic binding instance attr
    s.name = 'alice'
    print(s.name)

    # dynamic binding instance method
    s.set_age = MethodType(set_age, s)
    s.set_age(13)
    print(s.age)

    # dynamic binding class method
    Student.set_score = set_score
