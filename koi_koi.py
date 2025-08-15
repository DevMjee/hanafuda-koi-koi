"""Module to setup koi-koi hands, scoring piles, table, and deck"""
import random
import hanafuda
import gui


class Player:
    """Class defining current player hand, card pickups, and score across rounds"""

    def __init__(self, name='', hand=None, collected=None, sets=None, score=0, final_score=0):
        if hand is None and collected is None and sets is None:
            self.hand = []
            self.collected = []
            self.sets = {}
            self.koi = False
        self.name = name
        self.score = score
        self.final_score = final_score

    def match(self, card, matches):
        """function to check if cards have matching months on table"""
        if len(matches) == 3:  # case where the entire month can be picked up at once
            self.update_cards(card, matches)
            print('\nCOMPLETE MONTH MATCH!')

        else:  # match one card with one table match
            gui.display_contents(matches, 'match available')
            match = matches[gui.validate_input(
                'Which card on the table would you like to match with?', len(matches))]
            self.update_cards(card, match)
            print('\nMATCH!')

        # display updated win list before handover
        gui.display_contents(self.collected, 'updated win pile')

    def update_cards(self, card, match=None, skip=False):
        """function to update cards in hand and table to collected"""
        self.hand.remove(card)
        if isinstance(match, list):  # for full month match
            for month_card in match:
                table.contents.remove(month_card)
                self.collected.append(month_card)
            self.collected.append(card)
        else:  # single card match
            if skip:  # if skip, only add to table, no match needed (None)
                table.contents.append(card)
            else:  # update of collection and removal from table
                table.contents.remove(match)
                self.collected.extend([card, match])

    def list_matches(self, card):
        """function to obtain list of matches from table based on card month"""
        matches = [
            match for match in table.contents if match.month == card.month]
        return matches

    def draw(self):
        """function to draw card and match or add to table"""
        card = deck.contents.pop()  # draw new card and remove from deck (popping)
        print('\nNEW CARD DRAWN')
        print(card)

        matches = self.list_matches(card)
        if matches:
            # add to hand only if match available, will remove in update_cards
            self.hand.append(card)
            self.match(card, matches)

        else:
            print('\nNO MATCHES...')
            table.contents.append(card)

    # too many conditionals: check how to refactor the remaining player functions here? #

    def check_win(self, koi):
        """function to track sets and score"""
        win, cherry, moon, rain = False, False, False, False
        for rarity, card_set in enumerate(hanafuda.types):
            cards_from_set = [
                card for card in self.collected if card.yaku == card_set]
            set_count = len(cards_from_set)

            # using to track which score to add: higher rarity = more points for less (chaff = 0, light = 3)
            if rarity == 0:  # chaff
                # check special sets - not for chaff, but for seeds and light
                for card in cards_from_set:
                    # currently allowing sake cup to fit in multiple sets at one time - too strong? should it be one (strongest set) at a time?
                    if card.sake_cup:
                        self.sets['sake'] = None  # store to track existence

                # check set limit reached and if newly obtained
                if card_set in self.sets:
                    if self.sets[card_set] < set_count:
                        self.score += set_count - 10  # adds only 1 per new chaff
                        print(f'\n{card_set} SET WON!')
                        win = True

                elif set_count >= 10:
                    self.score += set_count - 9  # adds 1 + 1 per extra chaff
                    # for koi koi phase tracking
                    self.sets[card_set] = set_count
                    print(f'\n{card_set.upper()} SET WON!')
                    win = True

            elif rarity == 1:  # poetry
                # check special sets - must check all as 'if'
                blues = len(
                    [card for card in cards_from_set if card.blue])
                reds = len(
                    [card for card in cards_from_set if card.red])
                if blues == 3 and 'blue' not in self.sets:
                    self.score += 5
                    self.sets['blue'] = None  # store to track win
                    print(f'\nBLUE {card_set.upper()} SET WON!')
                    win = True

                if reds == 3 and 'red' not in self.sets:
                    self.score += 5
                    self.sets['red'] = None  # store to track win
                    print(f'\nRED {card_set.upper()} SET WON!')
                    win = True

                # check set limit reached and if newly obtained
                if card_set in self.sets:
                    if self.sets[card_set] < set_count:
                        self.score += set_count - 5  # adds only 1 per new poetry
                        print(f'\n{card_set.upper()} SET WON!')
                        win = True

                elif set_count >= 5:
                    self.score += set_count - 4  # adds 1 + 1 per extra poetry
                    # for koi koi phase tracking
                    self.sets[card_set] = set_count
                    print(f'\n{card_set.upper()} SET WON!')
                    win = True

            elif rarity == 2:  # seeds
                # check special sets
                if 'sake' in self.sets:  # counts as seeds as well
                    set_count += 1

                animals = len(
                    [card for card in cards_from_set if card.animal])
                if animals == 3 and 'animal' not in self.sets:
                    self.score += 5
                    # store only to track win, not score
                    self.sets['animal'] = None
                    print(f'\nANIMAL {card_set.upper()} SET WON!')
                    win = True

                # check set limit reached and if newly obtained
                if card_set in self.sets:
                    if self.sets[card_set] < set_count:
                        self.score += set_count - 5  # adds only 1 per new seeds
                        print(f'\n{card_set.upper()} SET WON!')
                        win = True

                elif set_count >= 5:
                    self.score += set_count - 4  # adds 1 + 1 per extra seeds
                    # for koi koi phase tracking
                    self.sets[card_set] = set_count
                    print(f'\n{card_set.upper()} SET WON!')
                    win = True

            elif rarity == 3:  # light
                # check special sets - other light sets don't add cumulative score, prefer rarest set
                for card in cards_from_set:
                    if card.rain:
                        rain = True
                    if card.moon:
                        moon = True
                    if card.cherry:
                        cherry = True

                # can have both viewings added with lights
                if cherry and 'sake' in self.sets and 'cherry' not in self.sets:
                    self.score += 5
                    self.sets['cherry'] = None
                    print(f'\nCHERRY VIEWING {card_set.upper()} SET WON!')
                    win = True
                if moon and 'sake' in self.sets and 'moon' not in self.sets:
                    self.score += 5
                    self.sets['moon'] = None
                    print(f'\nMOON VIEWING {card_set.upper()} SET WON!')
                    win = True

                # don't add scores here, only add the highest at TRIGGER WIN game end - 10, 7, 8, 6
                if set_count == 5 and 'five' not in self.sets:
                    self.sets['five'] = None
                    print(f'\nFIVE {card_set.upper()} SET WON!')
                    win = True

                elif set_count == 4 and 'four' not in self.sets:
                    if rain and 'rain' not in self.sets:
                        self.sets['rain'] = None
                        print(f'\nRAINY FOUR {card_set.upper()} SET WON!')
                        win = True

                    else:
                        self.sets['four'] = None
                        print(f'\nFOUR {card_set.upper()} SET WON!')
                        win = True

                elif set_count == 3 and 'three' not in self.sets:
                    self.sets['three'] = None
                    print(f'\nTHREE {card_set.upper()} SET WON!')
                    win = True

        if win:  # check if winner identified
            if koi:  # if already in koi koi phase
                choice = 1  # end game
            else:  # else offer koi koi
                gui.display_contents(('Call Koi-Koi', 'End Round'),
                                     'winning player options')
                choice = gui.validate_input(
                    'Would you like to call Koi-Koi?', 2)
            if choice == 0:
                return True  # enable koi koi phase
            else:
                return self.tally_player_score()  # end game, return winner
        else:  # if not a winner
            return  # None

    def tally_player_score(self):
        """function to add final light scores and continue if rounds remain"""
        print('\nENDING ROUND...')
        if 'five' in self.sets:
            self.score += 10
        elif 'four' in self.sets:
            self.score += 8
        elif 'rain' in self.sets:
            self.score += 7
        elif 'three' in self.sets:
            self.score += 6

        # score doubles if >= 7
        if self.score >= 7:
            self.score *= 2

        print(f'\nROUND SCORE: {self.score}')
        return self


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


def sort_by_month(cards):
    """function to sort objects in lists by their month value"""
    return sorted(cards, key=lambda card: card.month)


def shuffle_cards(players):
    """creates deck and distributes hands, for resetting rounds"""
    # create a randomly shuffled deck of cards
    new_deck = Pile(hanafuda.cards)
    random.shuffle(new_deck.contents)

    # distribute cards to table and player hands, update deck
    new_table = Pile(sort_by_month(random.sample(new_deck.contents, 8)))
    new_deck.contents = new_deck.remove_cards(new_table.contents)
    for player in players:
        # sort initial hands and table so user can read contents easier
        player.hand.extend(random.sample(new_deck.contents, 8))
        player.hand = sort_by_month(player.hand)
        new_deck.contents = new_deck.remove_cards(player.hand)

    return new_deck, new_table


deck, table = None, None  # space holders to use in functions


if __name__ == '__main__':
    if len(deck.contents) == 24:
        print("All ok! Cards successfully created.")
    else:
        print('ERROR: Incorrect deck size and setup for koi-koi.')
