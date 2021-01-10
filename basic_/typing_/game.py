import random
from typing import List, Tuple, NoReturn, Sequence, Any, TypeVar, Optional

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

## type aliases typically used for composite Type

# a tuple is an immutable sequence, and typically consists of a fixed number of possibly differently typed elements,
# so there are n (which is equal to the number of tuple's elements Type) Type hints inside the brackets
Card = Tuple[str, str]

# A list is a mutable sequence and usually consists of an unknown number of elements of the same type,
# so there is one Type hint inside the brackets
Deck = List[Card]


def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


# restrict choose() to be used for either str or Card:
Choosable = TypeVar("Choosable", str, Card)


def choose(items: Sequence[Choosable]) -> Choosable:
    """Choose and return a random item"""
    return random.choice(items)


# def player_order(names: Sequence[str], start: Optional[str] = None) -> Sequence[str]:
# the above annotate can be shorten as following, Mypy assumes that a default argument of None indecates an Optional argument
# even if the type hint does not explicitly say no.
def player_order(names: Sequence[str], start: str = None) -> Sequence[str]:
    """Rotate player order so that start goes first"""
    # if start is None:
    #     start = choose(names)
    start_idx = names.index(start)
    return (*names[start_idx:], *names[:start_idx])


# function without return values
def play() -> None:
    """Play a 4-player card game"""
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(create_deck(shuffle=True)))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    # turn_order = player_order(names)
    # Randomly play card from each player's hand until empty
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<4}", end="")
        print()


# Since black_hole() always raises an exception, it will never return properly.
def black_hole() -> NoReturn:
    raise Exception("There is no going back ...")


if __name__ == '__main__':
    play()
    # black_hole()
