#!/usr/bin/env python3
#


class Builder:
    def __init__(self):
        self.extra_cheese = False
        self.garlic = False

    def add_garlic(self):
        pass

    def add_extra_cheese(self):
        pass

    def build(self):
        pass


class _Pizza:
    def __init__(self, builder: Builder) -> None:
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self) -> str:
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = (f"Garlic: {garlic}", f"Extra cheese: {cheese}")
        return '\n'.join(info)

    class PizzaBuilder(Builder):
        def __init__(self):
            super().__init__()

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return _Pizza(self)


def createPizza():
    return _Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()


if __name__ == '__main__':
    print(createPizza())
