"""Module to play koi-koi with hanafuda"""
import hanafuda
import koi_koi


def make_move(player):
    """function to define choices turn player can make"""
    for card in player.hand:
        print(card)


def play_game(player_1, player_2):
    """function to simulate games between different players"""
    make_move(player_1)


if __name__ == '__main__':
    play_game(koi_koi.player_1, koi_koi.player_2)
