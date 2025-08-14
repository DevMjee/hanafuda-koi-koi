"""Module to play koi-koi with hanafuda"""
import random
import koi_koi
import gui

# still need to implement
# - lucky hand detection and implementation
# - create bot player for computer vs human
# - UPDATE README to include instructions and summary of game with screenshots and python version


def make_move(player, table):
    """function to define choices turn player can make"""

    # display current player hand and table
    gui.display_contents(player.hand, 'cards in hand')
    gui.display_contents(table, 'cards on table')
    gui.display_contents(('Pick Card Up', 'Put Card Down'), 'player options')

    while True:
        move_choice = gui.validate_between_two(
            player, 'Would you like to pick up or put down a card?')
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


def play_game(players):
    """function to simulate games between different players"""
    # below is for koi-koi
    rounds = 3  # number of rounds - base option is 3, should be validate_input() here for 3, 6, or 12
    winner = False
    for round_num in range(rounds):
        koi = False  # initialise to track when entering koi-koi round phase
        playing = True
        if winner:  # winner of last round should go first in turn order
            players.insert(0, players.pop(players.index(winner)))
            winner = False
        else:  # randomly assign a player to move first
            random.shuffle(players)

        for player in players:  # reset score and tracked sets at start of round
            player.score, player.sets, player.collected = 0, {}, []
        # reset deck and table at start of round
        koi_koi.deck, koi_koi.table = koi_koi.shuffle_cards(players)

        while playing:
            for index, player in enumerate(players, start=1):
                print('\n' * 32)
                if koi:
                    print('**** KOI-KOI CALLED! ****')

                # get up to date opponent win pile
                opponent = [other for other in players if other != player]
                print(
                    f"PLAYER {index}'s TURN. \nYOUR POINTS SECURED: {player.final_score}\nRIVAL'S POINTS SECURED: {opponent[0].final_score}")

                # always display both win piles
                gui.display_contents(player.collected, 'your current win pile')
                gui.display_contents(
                    opponent[0].collected, "rival's win pile")

                # actual move choice
                make_move(player, koi_koi.table.contents)

                player.draw()
                gui.display_contents(koi_koi.table.contents, 'updated table')

                if koi:
                    if isinstance(player.check_win(koi), str):
                        print('\n### GAME OVER ###\n')
                        playing = False
                        break
                else:
                    # koi can be False, True, or 'end'
                    koi = player.check_win(koi)

                if isinstance(koi, str):
                    print('\n### ROUND OVER ###\n')
                    player.final_score += player.score
                    winner = player
                    playing = False
                    break
                # check opponent hand is empty as well to end for empty hand
                elif not opponent[0].hand:
                    print(
                        '\n### HAND EMPTY, NO SET MADE, NO POINTS, ENDING GAME... ###\n')
                    print('\n### ROUND OVER ###\n')
                    playing = False
                    break
                else:
                    print('\n' * 8)
                    input(
                        'Press the enter key to end turn and pass to the next player.\n')

        # End round print of scores
        player_scores = []
        for index, player in enumerate(players, start=1):
            player_scores.append(player.final_score)
            print(
                f'\nPLAYER {index} SCORE FOR ROUND {round_num+1}: {player.final_score}\n')
        print(f'END OF ROUND {round_num+1}')
        input('Press enter to continue.')

    # Endgame print winner
    print('\n' * 8)
    print('GAME OVER')
    if player_scores[0] > player_scores[1]:
        print('PLAYER 1 WINS!')
    else:
        print('PLAYER 2 WINS!')


if __name__ == '__main__':
    play_game([koi_koi.player_1, koi_koi.player_2])
