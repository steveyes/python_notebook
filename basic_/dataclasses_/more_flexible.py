from dataclasses import dataclass, field, fields
from typing import List

_RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
_SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in _SUITS for r in _RANKS]


@dataclass(order=True)
class PlayingCard:
    # Comparing
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (_RANKS.index(self.rank) * len(_SUITS) + _SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


@dataclass
class Deck:
    # default_value
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    # Representation
    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})


if __name__ == '__main__':
    print(fields(Position))
    lat_unit = fields(Position)[2].metadata['unit']
    print(lat_unit)

    queen_of_hearts = PlayingCard('Q', '♡')
    ace_of_spades = PlayingCard('A', '♠')
    print(ace_of_spades > queen_of_hearts)
    print(Deck())
