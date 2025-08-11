"""Module to play koi-koi with hanafuda"""
import os
import koi_koi
import gui


def make_move(player, table):
    """function to define choices turn player can make"""

    print('\n### CARDS IN HAND ###')
    gui.print_choices(player.hand)

    print('\n### CARDS ON TABLE ###')
    gui.print_choices(table)

    print('\n### TURN MOVE CHOICES ###')
    gui.print_choices(('Pick Card Up', 'Put Card Down'))
    while True:
        try:
            move_choice = int(
                input('\nWould you like to pick up or put down a card?\n'))
            if move_choice == 1:  # pick up and draw
                # need to implement check to see if any matches available, else forced skip
                gui.validate_input(player, table)
                break
            elif move_choice == 2:  # put down and draw
                # discard = player.something() - which card to discard?
                # add to table, then draw, then break
                player.skip()
                break
            else:
                print(player.hand[100])  # force index error if out of range(2)

        except ValueError as err:
            print(f'\n[ERROR: {err}] \nPlease enter an integer value')

        except IndexError as err:
            print(f'[ERROR: {err}] \nPlease enter a value between 1 and 2')


def play_game(players):
    """function to simulate games between different players"""
    while True:
        for index, player in enumerate(players, start=1):
            print(f"### PLAYER {index}'S TURN ###")

            # always display both win piles
            print('\n### YOUR CURRENT WIN PILE ###')
            gui.print_choices(player.collected)
            print('\n### OPPONENT WIN PILE ###')
            opponent = [other for other in players if other != player]
            gui.print_choices(opponent[0].collected)

            # actual move choice
            make_move(player, koi_koi.table.contents)
            player.draw()

            if input('\nContinue to next player?') == 'no':
                break
            else:
                os.system('cls')  # clear to stop hand peeking at turn handover


if __name__ == '__main__':
    os.system('cls')
    play_game((koi_koi.player_1, koi_koi.player_2))
