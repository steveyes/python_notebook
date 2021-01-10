from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Person:
    name: str


def bulk_encode(_persons):
    persons = [Person(n) for n in _persons]
    return Person.schema().dumps(persons, many=True)


def bulk_decode():
    pass


if __name__ == '__main__':
    persons_json = bulk_encode(('alice', 'bob'))
    print(persons_json)
    print(type(persons_json))
    persons = Person.schema().loads(persons_json, many=True)
    print(persons)
    print(type(persons))
   