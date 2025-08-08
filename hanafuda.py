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


class Card:
    """Class representing the month a card represents"""

    def __init__(self, month):
        self.month = month


class Chaff(Card):
    """Class representing rules for Chaff scoring cards"""

    def __init__(self, month, sake_cup=False):
        super().__init__(month)
        self.sake_cup = sake_cup


class Poetry(Card):  # 'Blue', 'Red'
    """Class representing rules for Poetry scoring cards"""

    def __init__(self, month, blue=False, red=False):
        super().__init__(month)
        self.blue = blue
        self.red = red


class Seeds(Card):  # 'Boar-Deer-Butterfly' = animals (let birds != animals)
    """Class representing rules for Seeds scoring cards"""

    def __init__(self, month, animal=False):
        super().__init__(month)
        self.animal = animal


class Light(Card):  # 'Rain', 'Moon', 'Cherry'
    """Class representing rules for Light scoring cards"""

    def __init__(self, month, rain=False, moon=False, cherry=False):
        super().__init__(month)
        self.rain = rain
        self.moon = moon
        self.cherry = cherry


months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec')

types = ('chaff_1', 'chaff_2', 'poetry', 'seeds', 'light', 'chaff_3')

cards = (  # each dict is a month, each key-value pair is unique card
    # jan
    {types[0]: Chaff(months[0]), types[1]: Chaff(months[0]),
     types[2]: Poetry(months[0], red=True), types[4]: Light(months[0])},
    # feb
    {types[0]: Chaff(months[1]), types[1]: Chaff(months[1]),
     types[2]: Poetry(months[1], red=True), types[3]: Seeds(months[1])},
    # mar
    {types[0]: Chaff(months[2]), types[1]: Chaff(months[2]),
     types[2]: Poetry(months[2], red=True), types[4]: Light(months[2], cherry=True)},
    # apr
    {types[0]: Chaff(months[3]), types[1]: Chaff(months[3]),
     types[2]: Poetry(months[3]), types[3]: Seeds(months[3])},
    # may
    {types[0]: Chaff(months[4]), types[1]: Chaff(months[4]),
     types[2]: Poetry(months[4]), types[3]: Seeds(months[4])},
    # jun
    {types[0]: Chaff(months[5]), types[1]: Chaff(months[5]),
     types[2]: Poetry(months[5], blue=True), types[3]: Seeds(months[5], animal=True)},
    # jul
    {types[0]: Chaff(months[6]), types[1]: Chaff(months[6]),
     types[2]: Poetry(months[6]), types[3]: Seeds(months[6], animal=True)},
    # aug
    {types[0]: Chaff(months[7]), types[1]: Chaff(months[7]),
     types[3]: Seeds(months[7]), types[4]: Light(months[7], moon=True)},
    # sep
    {types[0]: Chaff(months[8]), types[1]: Chaff(months[8]),
     types[2]: Poetry(months[8], blue=True), types[5]: Chaff(months[8], sake_cup=True)},
    # oct
    {types[0]: Chaff(months[9]), types[1]: Chaff(months[9]),
     types[2]: Poetry(months[9], blue=True), types[3]: Seeds(months[9], animal=True)},
    # nov
    {types[0]: Chaff(months[10]), types[2]: Poetry(months[10]),
     types[3]: Seeds(months[10]), types[4]: Light(months[10], rain=True)},
    # dec
    {types[0]: Chaff(months[11]), types[1]: Chaff(months[11]),
     types[5]: Chaff(months[11]), types[4]: Light(months[11])}
)
