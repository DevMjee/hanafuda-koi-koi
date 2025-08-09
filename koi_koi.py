"""Module to setup koi-koi hands, scoring piles, table, and deck"""
import random
import hanafuda


class Player:
    """Class defining current player hand, card pickups, and score across rounds"""

    def __init__(self, hand=None, collected=None, score=0):
        if hand is None and collected is None:
            self.hand = []
            self.collected = []
        self.score = score

    def match(self, card, match):
        """function to check if cards have matching months"""
        if card.month == match.month:
            self.update_cards(card, match)
            return True
        else:
            return False

    def update_cards(self, card, match):
        """function to update cards in hand and table to collected"""
        self.hand.remove(card)
        table.contents.remove(match)
        self.collected.extend([card, match])

    def draw(self, card, table_choices):
        """function to draw card and match or add to hand"""
        print('### NEW CARD DRAWN ###')
        print(card)
        choices = list(
            choice for choice in table_choices if choice.month == card.month)
        if choices:
            print('### DRAW MATCH! ###')
            for index, choice in enumerate(choices, start=1):
                print(f'[{index}] - {choice}')
            while True:
                try:  # try to accept integer inputs and compare the card months
                    final_choice = choices[int(
                        input('Which card on the table would you like to match with?\n'))-1]
                    if player.match(card, final_choice):
                        break
                    else:  # except if not an integer repeat while loop
                        print('ERROR - something went wrong, this should not print.')
                except ValueError:
                    print('Please enter two valid indices.')
        else:
            print('### NO MATCHES, ADDING TO TABLE... ###')
            table.contents.append(card)


class Pile:
    """Class defining stack of cards"""

    def __init__(self, contents=None):
        if contents is None:
            self.contents = []
        else:
            self.contents = list(contents)

    def __str__(self):
        return f'Contents: {self.contents}'

    def remove_cards(self, to_remove):
        """function to update pile contents using another list"""
        return list(filter(lambda card: card not in to_remove, self.contents))


# initialise players
player_1 = Player()
player_2 = Player()

# create a randomly shuffled deck of cards
deck = Pile(hanafuda.cards)
random.shuffle(deck.contents)

# distribute cards to table and player hands, update deck
table = Pile(random.sample(deck.contents, 8))
deck.contents = deck.remove_cards(table.contents)
for player in (player_1, player_2):
    player.hand.extend(random.sample(deck.contents, 8))
    deck.contents = deck.remove_cards(player.hand)


if __name__ == '__main__':
    if len(deck.contents) == 24:
        print("All ok! Cards successfully created.")
    else:
        print('ERROR: Incorrect deck size and setup for koi-koi.')
