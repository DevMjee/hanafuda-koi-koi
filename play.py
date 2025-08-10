"""Module to play koi-koi with hanafuda"""
import os
import koi_koi
import gui


def make_move(player, table):
    """function to define choices turn player can make"""

    print('\n### CARDS IN HAND ###')
    gui.print_cards(player.hand)

    print('\n### CARDS ON TABLE ###')
    gui.print_cards(table)

    gui.validate_input(player, table)


def play_game(players):
    """function to simulate games between different players"""
    while True:
        for index, player in enumerate(players, start=1):
            print(f"### PLAYER {index}'S TURN ###")

            # always display both win piles
            print('\n### YOUR CURRENT WIN PILE ###')
            gui.print_cards(player.collected)
            print('\n### OPPONENT WIN PILE ###')
            opponent = [other for other in players if other != player]
            gui.print_cards(opponent[0].collected)

            # actual move choice
            make_move(player, koi_koi.table.contents)
            player.draw(koi_koi.table.contents)

            # display updated win list before handover
            print('\n### UPDATED WIN PILE ###')
            gui.print_cards(player.collected)

            if input('\nContinue to next player?') == 'no':
                break
            else:
                os.system('cls')  # clear to stop hand peeking at turn handover


if __name__ == '__main__':
    os.system('cls')
    play_game((koi_koi.player_1, koi_koi.player_2))
