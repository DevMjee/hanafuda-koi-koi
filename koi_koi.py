"""Module to setup koi-koi hands, scoring piles, table, and deck"""
import random
import hanafuda


class Player():
    """Class defining current player hand, card pickups, and score across rounds"""

    def __init__(self, hand=None, pile=None, score=0):
        if hand is None and pile is None:
            self.hand = []
            self.pile = []
        self.score = score


# shuffle the deck of cards
deck = list(hanafuda.cards)
random.shuffle(deck)

to_distribute = random.sample(deck, 24)
deck -= to_distribute


player_1 = Player()
player_2 = Player()

table = {}
player_1.hand = {}


if __name__ == '__main__':
    print(deck)
