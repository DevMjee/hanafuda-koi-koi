# Classes to define cards

# Alternative games: Hawaii Go-Stop and Hawaii Higo-Bana

# Sets to define
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
# 8 pairs of 4 months   = 6 points + instant win - 4 pairs

# if points > 7, double score
# 48 total cards
# - 5 lights
# - 9 seeds
# - 10 poetry
# - 24 chaff

class Card:
    def __init__(self, month, family):
        self.month = month
        self.family = family


class Chaff(Card):
    def __init__(self, month, family):
        super().__init__(month, family)


class Poetry(Card):  # 'Blue', 'Red'
    def __init__(self, month, family):
        super().__init__(month, family)


class Seeds(Card):  # 'Boar-Deer-Butterfly'
    def __init__(self, month, family):
        super().__init__(month, family)


class Light(Card):  # 'Three', 'Rain', 'Four', 'Five'
    def __init__(self, month, family):
        super().__init__(month, family)


class Cup(Chaff, Seeds):  # 'Moon', 'Cherry'
    def __init__(self, month, family):
        super().__init__(month, family)


months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

family_sets = ('Chaff', 'Poetry', 'Seeds', 'Light')


cards = {
    'jan_chaff_1': Chaff(months[0]) 'jan_chaff_2', 'jan_red',
    'jan_light' 'feb_chaff_1', 'feb_chaff_2', 'mar'}

for card in
jan_chaff_1 = Chaff(months[0], family_sets[0])
jan_chaff_2 = Card(months[0], family_sets[0])

deck = []
# define a deck list with all cards in order

if __name__ == '__main__':
    for score in score_sets:
        print(score)
