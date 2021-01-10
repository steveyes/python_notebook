from typing import Iterable


class Foo(object):
    mapping = {
        'attr1': 1,
        'attr2': 2,
        'attr3': 3,
    }

    def __getattr__(self, item):
        if item in self.mapping:
            return self.mapping[item]

    def __dir__(self) -> Iterable[str]:
        return self.mapping.keys()


if __name__ == '__main__':
    foo = Foo()
    print(foo.__getattr__('attr1'))
    print(getattr(foo, 'attr2'))
    # will lookup stub of class Foo from sample_.pyi
    print(foo.attr3)
    print(getattr(foo, 'attr4', 4))

    print(dir(foo))
    print(foo.attr1)
