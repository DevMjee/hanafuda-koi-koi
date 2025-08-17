"""Module to setup koi-koi hands, scoring piles, table, and deck"""
import random
import hanafuda
import gui

# Yaku (scoring sets)
# 10 Chaff              = 1 point (+1 per)
# 5 Poetry              = 1 point (+1 per)
# 5 Seeds               = 1 point (+1 per)
# 3 (all) Blue Poetry   = 5 points
# 3 (all) Red Poetry    = 5 points
# 3 Boar-Deer-Butterfly = 5 points
# 2 Moon Viewing        = 5 points
# 2 Cherry Viewing      = 5 points
# 3 Three Lights        = 6 points
# 4 Rainy Four Lights   = 7 points
# 4 Four Lights         = 8 points
# 5 (all) Five Lights   = 10 points

# Instant win hands to start with
# 4 (all) of a month    = 6 points + instant win - 4 of a kind
# 4 pairs of 4 months   = 6 points + instant win - 4 pairs

# if points > 7, double score
# 48 total cards
# - 5 lights
# - 9 seeds
# - 10 poetry
# - 24 chaff

# As soon as a set is made by either person, round pauses
# First winning player can choose to call koi-koi to increase points
# Round ends when another set is made or existing one is added to
# Whichever player makes the set and ends the round wins
# Only the winning player tracks points earned in round
# Rounds can be 3, 6 or 12


class Player:
    """Class defining current player hand, card pickups, and score across rounds"""

    def __init__(self, name='', hand=None, collected=None, sets=None, score=0, final_score=0):
        if hand is None and collected is None and sets is None:
            self.hand = []
            self.collected = []
            self.sets = {}
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
        win = False  # define here in case of empty list
        sake = False
        # only loop through first four main types: chaff, poetry, seeds, light
        for rarity, card_set in enumerate(hanafuda.types[:4]):
            cards_from_set = [
                card for card in self.collected if card.yaku == card_set]
            set_count = len(cards_from_set)

            # rarity tracks set: higher rarity = more points (chaff = 0, light = 3)
            if rarity == 0 and cards_from_set:  # chaff
                # check special sets - not for chaff, but for seeds and light
                for card in cards_from_set:
                    if card.sake_cup:
                        sake = True

                # check chaff set
                if self.check_limit_reached(card_set, set_count, 10):
                    win = True  # do not set directly True, else will remove wins from other sets

            elif rarity == 1 and cards_from_set:  # poetry
                # check special sets - must check all as 'if'
                blues = len(
                    [card for card in cards_from_set if card.blue])
                if blues == 3 and hanafuda.types[4] not in self.sets:
                    self.sets[hanafuda.types[4]] = 5  # store to track win
                    gui.print_win(card_set, hanafuda.types[4])
                    win = True

                reds = len(
                    [card for card in cards_from_set if card.red])
                if reds == 3 and hanafuda.types[5] not in self.sets:
                    self.sets[hanafuda.types[5]] = 5  # store to track win
                    gui.print_win(card_set, hanafuda.types[5])
                    win = True

                # check poetry standard set
                if self.check_limit_reached(card_set, set_count, 5):
                    win = True

            elif rarity == 2 and cards_from_set:  # seeds
                # check special sets
                if sake:  # sake cup counts as seeds as well
                    set_count += 1

                animals = len(
                    [card for card in cards_from_set if card.animal])
                if animals == 3 and hanafuda.types[6] not in self.sets:
                    # store only to track win, not score
                    self.sets[hanafuda.types[6]] = 5
                    gui.print_win(card_set, hanafuda.types[6])
                    win = True

                # check seeds standard set
                if self.check_limit_reached(card_set, set_count, 5):
                    win = True

            elif rarity == 3 and cards_from_set:  # light
                # check special sets with flags
                rain, moon, cherry = False, False, False
                for card in cards_from_set:
                    if card.rain:
                        rain = True
                    if card.moon:
                        moon = True
                    if card.cherry:
                        cherry = True

                # can have both viewings added with lights
                if sake:  # check viewing sets with flags
                    if cherry and hanafuda.types[7] not in self.sets:
                        self.sets[hanafuda.types[7]] = 5
                        gui.print_win(card_set, hanafuda.types[7])
                        win = True

                    if moon and hanafuda.types[8] not in self.sets:
                        self.sets[hanafuda.types[8]] = 5
                        gui.print_win(card_set, hanafuda.types[8])
                        win = True

                # check standard light sets
                if set_count == 5 and hanafuda.types[9] not in self.sets:
                    self.sets[hanafuda.types[9]] = 10
                    gui.print_win(card_set, hanafuda.types[9])
                    win = True

                elif set_count == 4 and hanafuda.types[10] not in self.sets:
                    # check for rain
                    if rain and hanafuda.types[11] not in self.sets:
                        self.sets[hanafuda.types[11]] = 7
                        gui.print_win(card_set, hanafuda.types[11])
                        win = True

                    else:
                        self.sets[hanafuda.types[10]] = 8
                        gui.print_win(card_set, hanafuda.types[10])
                        win = True

                elif set_count == 3 and hanafuda.types[12] not in self.sets:
                    self.sets[hanafuda.types[12]] = 6
                    gui.print_win(card_set, hanafuda.types[12])
                    win = True

        if win:  # check if winner identified
            if koi or not self.hand:  # check koi phase or empty hand
                choice = 1  # end game
            else:  # else offer koi koi
                gui.display_contents(('Call Koi-Koi', 'End Round'),
                                     'winning player options')
                choice = gui.validate_input(
                    'Would you like to call Koi-Koi?', 2)
            if choice == 0:
                return True  # enable koi koi phase
            else:
                return self.tally_player_score()  # end game, return winner score
        else:  # if not a winner
            return  # None

    def check_limit_reached(self, card_set, set_count, limit):
        """function to check if limit reached for standard set collections (chaff, poetry, seeds)"""
        # check set limit reached and if newly obtained
        if card_set in self.sets:
            if self.sets[card_set] < set_count:
                # track how many for scoring later
                self.sets[card_set] = set_count
                gui.print_win(card_set)
                return True

        # self.sets used for koi koi phase tracking
        elif set_count >= limit:
            self.sets[card_set] = set_count
            gui.print_win(card_set)
            return True

        else:
            return False

    def lucky_hand(self):
        """function to detect lucky hands at round start"""
        months = [card.month for card in self.hand]  # list of all months
        pairs = True  # flag to check for 4 pair hand

        #  check for full month in hand
        for month in months:
            if months.count(month) == 4:
                return True
            # not a pairs hand if any month count != 2
            elif months.count(month) != 2:
                pairs = False

        if pairs:  # after checking all months, must be pairs hand if still True
            return True

    def tally_player_score(self):
        """function to add final scores and continue if rounds remain"""
        print('\nENDING ROUND...')

        # flags to determine whether stronger set has been made or not if it exists
        seeds, poetry = True, True

        # reverse to check for stronger sets first
        for index, card_set in enumerate(reversed(hanafuda.types)):
            if card_set in self.sets:
                if index in range(6):  # add no bonuses for lights
                    self.score += self.sets[card_set]

                # add +1 bonuses for blue, red, animal sets - limits for each
                elif index in range(6, 9):
                    if index == 6:  # seeds animal
                        self.score += (self.sets[card_set] +
                                       self.sets[hanafuda.types[2]] - 3)
                        seeds = False
                    else:  # poetry blue and red
                        self.score += (self.sets[card_set] +
                                       self.sets[hanafuda.types[1]] - 3)
                        poetry = False
                elif index == 10:  # add 1 +1 for standard sets if no special sets
                    if seeds:
                        self.score += 1 + self.sets[hanafuda.types[2]] - 5
                elif index == 11:
                    if poetry:
                        self.score += 1 + self.sets[hanafuda.types[1]] - 5
                else:  # chaff
                    self.score += 1 + self.sets[hanafuda.types[0]] - 10

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
