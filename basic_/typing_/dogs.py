from __future__ import annotations
from datetime import date
from typing import Type, TypeVar

# We specify that Animal is an upper bound for TAnimal.
# Specifying bound means that TAnimal will only be Animal or one of its subclasses.
# This is needed to properly restrict the types that are allowed.
TAnimal = TypeVar("TAnimal", bound="Animal")


class Animal:

    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    # The typing.Type[] construct is the typing equivalent of type().
    # You need it to note that the class method expects a class and returns an instance of that class.
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        cls = self.__class__
        return cls(name, self.birthday)


class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")


fido = Dog.newborn('Fido')
pluto = fido.twin('Pluto')
fido.bark()
pluto.bark()

# While the code runs without problems, Mypy will flag a problem:
# dogs.py:27: error: "Animal" has no attribute "bark"
# dogs.py:28: error: "Animal" has no attribute "bark"
# Found 2 errors in 1 file (checked 1 source file)
# The issue is that even though the inherited Dog.newborn() and Dog.twin() methods will return a Dog the annotation says that they return an Animal.
