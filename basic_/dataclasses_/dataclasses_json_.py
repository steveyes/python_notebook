from dataclasses import dataclass
from dataclasses_json import dataclass_json, DataClassJsonMixin

"""install
pip install dataclasses-json
"""


@dataclass_json
@dataclass
class DecoratorExample:
    name: str
    age: int


def simple_():
    alice = DecoratorExample('alice', 18)
    alice_json = alice.to_json()
    print(alice_json)
    print(type(alice_json))

    alice_dict = alice.to_dict()
    print(alice_dict)
    print(type(alice_dict))

    print(DecoratorExample.from_json(alice_json))
    print(DecoratorExample.from_dict(alice_dict))


@dataclass
class MixinExample(DataClassJsonMixin):
    name: str
    age: int


def mixin_():
    alice = MixinExample('alice', 18)
    assert MixinExample.from_json(alice.to_json()) == alice


if __name__ == '__main__':
    simple_()
    mixin_()
