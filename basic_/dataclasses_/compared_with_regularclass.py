from dataclasses import dataclass


@dataclass
class DataClassCard:
    """A data class is a regular Python class. The only thing that sets it apart is that it has basic data model
    methods like .__init__(), .__repr__(), and .__eq__() implemented for you. """
    rank: str
    suit: str


class RegularCard:
    """Let RegularCard class to imitate the dataclass above, you need to add __repr__ and __eq__ below"""

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, o):
        if o.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (o.rank, o.suit)


if __name__ == '__main__':
    def demo_DataClassCard():
        queen_of_hearts = DataClassCard('Q', 'Hearts')
        print(queen_of_hearts)
        print(queen_of_hearts.rank)
        print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


    def demo_RegularCard():
        queen_of_hearts = RegularCard('Q', 'Hearts')
        print(queen_of_hearts)
        print(queen_of_hearts.rank)
        print(queen_of_hearts == RegularCard('Q', 'Hearts'))


    demo_DataClassCard()
    demo_RegularCard()
