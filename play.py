"""Module to play koi-koi with hanafuda"""
import random
import koi_koi
import gui


def make_move(player, table):
    """function to define choices turn player can make"""

    # display current player hand and table
    gui.display_contents(player.hand, 'cards in hand')
    gui.display_contents(table, 'cards on table')
    gui.display_contents(('Pick Card Up', 'Put Card Down'), 'player options')

    while True:
        move_choice = gui.validate_input(  # move choice to pick up or put down card for turn
            'Would you like to pick up or put down a card?', 2)
        if move_choice == 0:  # pick up and draw
            # check to see if any matches available, else move_choice again
            hand_choice = player.hand[gui.validate_input(
                'Which card would you like to play from your hand?', len(player.hand))]

            table_matches = player.list_matches(hand_choice)
            # ensure card selections are of matching months
            if table_matches:
                player.match(hand_choice, table_matches)
                return  # break loop
            else:  # if mismatched month
                print('\n[ERROR: invalid selection]')
                print(
                    f'\nPlease match the same month. {hand_choice.month} is not on the table.')

        elif move_choice == 1:  # put down and draw
            # add to table, then draw, then break
            hand_choice = player.hand[gui.validate_input(
                'Which card would you like to play from your hand?', len(player.hand))]
            # restrict putting down cards with existing match
            if player.list_matches(hand_choice):
                print('\n[ERROR: invalid selection]')
                print(
                    f'{hand_choice.month} is on the table. Please put down a card without a match.')

            else:  # put down card on table and draw one
                player.update_cards(hand_choice, skip=True)
                gui.display_contents(table, 'updated table')
                return  # break loop


# forces koi koi currently
def play_game(players):
    """function to simulate games between different players"""
    print('\nWelcome to Hanafuda (Koi-Koi)\n')

    # ask for number of rounds to play for between 3, 6, 9, and 12
    gui.display_contents([(str((num+1)*3) + ' Rounds')
                         for num in range(4)], 'game round options')
    # reobtain rounds number from validated input
    rounds = (gui.validate_input(
        'Please input the number of rounds you would like to play.', 4) + 1) * 3

    # initialise tracker for last round winner
    winner = None

    # loop for number of rounds selected
    for round_num in range(rounds):
        koi = None  # initialise to track which player enters koi-koi round phase
        playing = True  # initialise to track when playing ends for round

        # decide turn order
        if winner:  # winner of last round should go first in turn order
            players.insert(0, players.pop(players.index(winner)))
            winner = None
        else:  # randomly assign a player to move first if no winner
            random.shuffle(players)

        for player in players:  # reset score and tracked sets at start of round
            player.score, player.sets, player.collected, player.hand = 0, {}, [], []

        # reset deck and table at start of round
        koi_koi.deck, koi_koi.table = koi_koi.shuffle_cards(players)

        # check for lucky hands before continuing, only at start of round
        for player in players:
            if player.lucky_hand():
                playing = False
                gui.display_contents(player.hand, 'winning hand')
                print(f'\n{player.name} WINS: LUCKY HAND!\n')
                player.final_score += 6  # lucky hands award 6 points and end the round
                winner = player
                break

        while playing:
            for player in players:
                print('\n' * 32)  # 'clearscreen' for both windows and mac
                if koi:
                    print(f'**** KOI-KOI CALLED BY {koi.name.upper()}! ****')

                # get up to date opponent win pile by referring to opponent as rival[0]
                rival = [other for other in players if other != player]
                print(f"{player.name.upper()}'s TURN.")
                print(('-'*4) + f' YOUR POINTS: {player.final_score}')
                print(('-'*4) + f" RIVAL'S POINTS: {rival[0].final_score}")

                # always display both win piles
                gui.display_contents(player.collected, 'your current win pile')
                gui.display_contents(rival[0].collected, "rival's win pile")

                # actual move choice
                make_move(player, koi_koi.table.contents)
                player.draw()
                gui.display_contents(koi_koi.table.contents, 'updated table')

                # check if winner exists
                winner = player.check_win(koi)

                if winner:
                    # if winner is True, flag koi koi phase
                    if isinstance(winner, bool):
                        koi = player  # track who called koi koi for printing
                        winner = None
                    # if winner is a player, end round
                    else:
                        print('\nROUND OVER\n')
                        player.final_score += player.score
                        playing = False
                        break
                # check opponent hand is end for empty hand finish (tie)
                elif not rival[0].hand:
                    print(
                        '\nROUND OVER: HAND EMPTY, NO SET MADE, NO POINTS = TIE. ENDING ROUND...\n')
                    playing = False
                    break
                else:
                    print('\n' * 8)
                    input(
                        'Press the enter key to end turn and pass to the next player.\n')

        # End round print of scores
        for player in players:
            print(
                f'\n{player.name} SCORE FOR ROUND {round_num+1}: {player.final_score}\n')
        print(f'END OF ROUND {round_num+1} out of {rounds}')
        input('Press enter to continue.')

    # Endgame print winner
    print('\n' * 8)
    print('GAME OVER')
    # control final winner print for highest score or tie
    for player in players:
        if not winner:  # if most recent winner was a tie (None)
            winner = player
        else:  # record highest score as winner
            if player.final_score > winner.final_score:
                winner = player
            elif winner.final_score == player.final_score:
                winner = None  # flag for draw/tie at the end only

    if winner:
        print(f'\n{winner.name.upper()} WINS!\n')
    else:  # winner is still None after everything
        print("\nIT'S A DRAW!\n")


# edit more when more game options added
if __name__ == '__main__':
    # ...or default names
    name_1 = input('\nEnter Player 1\'s name:\n').strip() or 'Player 1'
    name_2 = input('\nEnter Player 2\'s name:\n').strip() or 'Player 2'

    # initialise players, deck, and table
    player_1 = koi_koi.Player(name=name_1)
    player_2 = koi_koi.Player(name=name_2)
    play_game([player_1, player_2])
