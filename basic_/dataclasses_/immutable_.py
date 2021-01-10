from dataclasses import dataclass
from typing import List

from example_.dataclasses_.more_flexible import PlayingCard


@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str


@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[PlayingCard]


if __name__ == '__main__':
    pos = Position('Oslo', 10.8, 59.9)
    # dataclasses.FrozenInstanceError: cannot assign to field 'name'
    # pos.name = 'Stockholm'

    # Even though both ImmutableCard and ImmutableDeck are immutable, the list holding cards is not. You can
    # therefore still change the cards in the deck:
    queen_of_hearts = ImmutableCard('Q', '♡')
    ace_of_spades = ImmutableCard('A', '♠')
    deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
    print(deck)
    deck.cards[0] = ImmutableCard('7', '♢')
    print(deck)


