import attr


def alternatives_01():
    # using these structures is not ideal
    queen_of_hearts_tuple = ('Q', 'Hearts')
    queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Heart'}
    print(queen_of_hearts_tuple[0])
    print(queen_of_hearts_dict['suit'])


def alternatives_02():
    from collections import namedtuple
    NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit', ])
    queen_of_hearts = NamedTupleCard('Q', 'Hearts')
    print(queen_of_hearts)
    print(queen_of_hearts.rank)
    print(queen_of_hearts == NamedTupleCard('Q', 'Hearts'))

    # a namedtuple is a regular tuple
    print(queen_of_hearts == ('Q', 'Hearts'))

    # lack of awareness about its own type can lead to subtle and hard-to-find bugs
    Person = namedtuple('Person', ['first_initial', 'last_name'])
    ace_of_spades = NamedTupleCard('A', 'Spades')
    print(ace_of_spades == Person('A', 'Spades'))

    # nature immutable
    card = NamedTupleCard('7', 'Diamonds')
    # AttributeError: can't set attribute
    # card.rank = '9'


@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()


card = AttrsCard('Q', 'Hearts')


def alternatives_03():
    print(card)
    print(card.rank)
    print(card == AttrsCard('Q', 'Hearts'))
    card.rank = 'A'


if __name__ == '__main__':
    alternatives_01()
    alternatives_02()
    alternatives_03()
