"""Module to play koi-koi with hanafuda"""
import hanafuda
import koi_koi


def make_move(player, table):
    """function to define choices turn player can make"""

    print('### CARDS IN HAND ###')
    for index, card in enumerate(player.hand, start=1):
        print(f'[{index}] - {card}')
    print('### CARDS ON TABLE ###')
    for index, card in enumerate(table, start=1):
        print(f'[{index}] - {card}')
    while True:
        hand = input('Which card would you like to play?\n')
        move = input('Which card on the table would you like to match with?\n')
        try:
            player.match(player.hand[int(hand)], table[int(move)])
            break
        except ValueError:
            print(
                f'Please enter two valid indices between 1 and {len(player.hand)} for your hand and between 1 and {len(table)} for the table.')


def play_game(player_1, player_2):
    """function to simulate games between different players"""
    make_move(player_1, koi_koi.table.contents)
    make_move(player_1, koi_koi.table.contents)


if __name__ == '__main__':
    play_game(koi_koi.player_1, koi_koi.player_2)
