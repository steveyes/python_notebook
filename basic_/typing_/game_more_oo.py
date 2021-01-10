# game_more_oo.py
from __future__ import annotations

import random
import sys
from typing import List


class Card:
    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.suit}{self.rank}"


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    @classmethod
    # in Python 3.7 and later, forward references are available through a __future__ import:
    # def create(cls, shuffle: bool = False) -> 'Deck':
    # With the __future__ import you can use Deck instead of "Deck" even before Deck is defined.
    def create(cls, shuffle: bool = False) -> Deck:
        """Create a new deck of 52 card"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    def deal(self, num_hands):
        """Deal the cards in the deck into a number of hands"""
        cls = self.__class__
        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))


class Player:
    def __init__(self, name: str, hand: Deck) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):
        """Play a card from the player's hand"""
        card = random.choice(self.hand.cards)
        self.hand.cards.remove(card)
        print(f"{self.name}: {card!r:<3} ", end="")
        return card


class Game:
    # Regarding type annotations: even though names will be a tuple of strings, you should only annotate the type of each name.
    # In other words, you should use str and not Tuple[str]:
    def __init__(self, *names: str) -> None:
        """Set up the deck and deal cards to 4 players"""
        deck = Deck.create(shuffle=True)
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
        self.hands = {n: Player(n, h) for n, h in zip(self.names, deck.deal(4))}

    def play(self):
        """Play a card game"""
        start_player = random.choice(self.names)
        turn_over = self.player_order(start=start_player)

        # Play cards from each player's hand until empty
        while self.hands[start_player].hand.cards:
            for name in turn_over:
                self.hands[name].play_card()
            print()

    def player_order(self, start):
        """Rotate player order so that start goes first"""
        if start is None:
            start = random.choice(self.names)
        start_idx = self.names.index(start)
        return self.names[start_idx:] + self.names[:start_idx]


if __name__ == '__main__':
    # Read player names from command line
    player_names = sys.argv[1:]
    game = Game(*player_names)
    game.play()

# TODO
# https://realpython.com/python-type-checking/#playing-with-python-types-part-2
# Type Hints for Methods
