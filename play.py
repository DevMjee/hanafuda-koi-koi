"""Module to play koi-koi with hanafuda"""
import koi_koi
import gui


def make_move(player, table):
    """function to define choices turn player can make"""

    # display current player hand and table
    gui.display_contents(player.hand, 'cards in hand')
    gui.display_contents(table, 'cards on table')
    gui.display_contents(('Pick Card Up', 'Put Card Down'), 'player options')

    while True:
        try:
            move_choice = int(
                input('\nWould you like to pick up or put down a card?\n'))
            if move_choice == 1:  # pick up and draw
                # need to implement check to see if any matches available, else forced skip
                card, match = gui.validate_input(player, table)
                if player.match(card, match):
                    return

            elif move_choice == 2:  # put down and draw
                # discard = player.something() - which card to discard?
                # add to table, then draw, then break
                card = gui.validate_input(player, table, skip=True)
                if player.skip(card):
                    gui.display_contents(
                        koi_koi.table.contents, 'updated table')
                    return

            else:
                print(player.hand[100])  # force index error if out of range(2)

        except ValueError as err:
            print(f'\n[ERROR: {err}] \nPlease enter an integer value')

        except IndexError as err:
            print(
                f'[ERROR: {err}] \nPlease enter a value between 1 [Pick Up] and 2 [Put Down]')


def play_game(players):
    """function to simulate games between different players"""
    while True:
        for index, player in enumerate(players, start=1):
            print('\n' * 32)
            gui.display_contents((), f"player {index}'s turn")

            # always display both win piles
            gui.display_contents(player.collected, 'your current win pile')
            # get up to date opponent win pile
            opponent = [other for other in players if other != player]
            gui.display_contents(opponent[0].collected, "opponent's win pile")

            # actual move choice
            make_move(player, koi_koi.table.contents)
            player.draw()
            gui.display_contents(koi_koi.table.contents, 'updated table')

            print('\n' * 8)
            input('Press any key to end turn and pass to the next player.\n')


if __name__ == '__main__':
    play_game((koi_koi.player_1, koi_koi.player_2))
