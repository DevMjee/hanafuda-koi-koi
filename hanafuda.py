"""Module defining hanafuda (flower cards)"""
# Alternative games: Hawaii Go-Stop and Hawaii Higo-Bana

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

import calendar


class Card:
    """Class representing the month and scoring set (yaku) for a card"""

    def __init__(self, month, yaku):
        self.month = month
        self.yaku = yaku

    def __str__(self):
        return f'{self.month} {self.yaku}'


class Chaff(Card):
    """Class representing rules for Chaff scoring cards"""

    def __init__(self, month, yaku, sake_cup=False):
        super().__init__(month, yaku)
        self.sake_cup = sake_cup

    def __str__(self):
        if self.sake_cup:
            return '¦ ' + super().__str__() + ': Sake Cup |'
        else:
            return '| ' + super().__str__() + ' |'


class Poetry(Card):  # 'Blue', 'Red'
    """Class representing rules for Poetry scoring cards"""

    def __init__(self, month, yaku, blue=False, red=False):
        super().__init__(month, yaku)
        self.blue = blue
        self.red = red

    def __str__(self):
        if self.blue:
            return '~ ' + super().__str__() + ': Blue ~'
        elif self.red:
            return '~ ' + super().__str__() + ': Red ~'
        else:
            return '~ ' + super().__str__() + ' ~'


class Seeds(Card):  # 'Boar-Deer-Butterfly' = animals (let birds != animals)
    """Class representing rules for Seeds scoring cards"""

    def __init__(self, month, yaku, animal=False):
        super().__init__(month, yaku)
        self.animal = animal

    def __str__(self):
        if self.animal:
            return '¦ ' + super().__str__() + ': Animal ¦'
        else:
            return '¦ ' + super().__str__() + ' ¦'


class Light(Card):  # 'Rain', 'Moon', 'Cherry'
    """Class representing rules for Light scoring cards"""

    def __init__(self, month, yaku, rain=False, moon=False, cherry=False):
        super().__init__(month, yaku)
        self.rain = rain
        self.moon = moon
        self.cherry = cherry

    def __str__(self):
        if self.rain:
            return '/ ' + super().__str__() + ': Rainy /'
        elif self.moon:
            return '* ' + super().__str__() + ': Moonlit *'
        elif self.cherry:
            return '* ' + super().__str__() + ': Cherry Blossom *'
        else:
            return '* ' + super().__str__() + ' *'


# initialise months list
months = calendar.month_name[1:]

# read set names (types) from file, rewrite file to change set names
# e.g. "bright" instead of "light" - note only first four entries are used
with open('yaku.txt', mode='r', encoding='utf-8') as file:
    types = file.read().split(',')

cards = (  # contains objects representing all 48 unique cards
    # jan
    Chaff(months[0], types[0]), Chaff(months[0], types[0]),
    Poetry(months[0], types[1], red=True), Light(months[0], types[3]),
    # feb
    Chaff(months[1], types[0]), Chaff(months[1], types[0]),
    Poetry(months[1], types[1], red=True), Seeds(months[1], types[2]),
    # mar
    Chaff(months[2], types[0]), Chaff(months[2], types[0]),
    Poetry(months[2], types[1], red=True),
    Light(months[2], types[3], cherry=True),
    # apr
    Chaff(months[3], types[0]), Chaff(months[3], types[0]),
    Poetry(months[3], types[1]), Seeds(months[3], types[2]),
    # may
    Chaff(months[4], types[0]), Chaff(months[4], types[0]),
    Poetry(months[4], types[1]), Seeds(months[4], types[2]),
    # jun
    Chaff(months[5], types[0]), Chaff(months[5], types[0]),
    Poetry(months[5], types[1], blue=True),
    Seeds(months[5], types[2], animal=True),
    # jul
    Chaff(months[6], types[0]), Chaff(months[6], types[0]),
    Poetry(months[6], types[1]), Seeds(months[6], types[2], animal=True),
    # aug
    Chaff(months[7], types[0]), Chaff(months[7], types[0]),
    Seeds(months[7], types[2]), Light(months[7], types[3], moon=True),
    # sep
    Chaff(months[8], types[0]), Chaff(months[8], types[0]),
    Poetry(months[8], types[1], blue=True),
    Chaff(months[8], types[0], sake_cup=True),
    # oct
    Chaff(months[9], types[0]), Chaff(months[9], types[0]),
    Poetry(months[9], types[1], blue=True),
    Seeds(months[9], types[2], animal=True),
    # nov
    Chaff(months[10], types[0]), Poetry(months[10], types[1]),
    Seeds(months[10], types[2]), Light(months[10], types[3], rain=True),
    # dec
    Chaff(months[11], types[0]), Chaff(months[11], types[0]),
    Chaff(months[11], types[0]), Light(months[11], types[3])
)
