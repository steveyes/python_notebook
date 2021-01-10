from typing import ClassVar, List


class MyClass:
    attr: int
    charge_percent: int = 100

    def __init__(self) -> None:
        ...

    def my_method(self, num: int, str1: str) -> str:
        return num * str1


mc: MyClass = MyClass()


# You can use the ClassVar annotation to declare a class variable
class Car:
    seats: ClassVar[int] = 4
    passengers = ClassVar[List[str]]


# You can also declare the type of an attribute in "__init__"
class Box:

    def __init__(self) -> None:
        self.item: List[str] = []

