"""Module for common functions to print cards and display game neatly"""


def print_cards(contents):
    """function to print and display cards neatly with spacing"""
    if contents:

        # print list of cards two at a time
        for index, card in enumerate(contents, start=1):
            if index % 2 == 0:
                continue
            else:
                hand_print = f'[{index}] - {card}'
                hand_print = hand_print.ljust(40)
                if card != contents[-1]:  # only pass if another card to display exists
                    hand_print += f'    [{index+1}] - {contents[index]}'
            print(hand_print)

    else:
        print('Empty!')


def validate_input(player, table, draw=False):
    """function to check valid integer inputs for working controls"""
    while True:
        try:  # try to accept integer inputs and compare the card months
            if draw:  # during turn draw
                hand_choice = draw
            else:  # during turn play
                hand_choice = player.hand[int(
                    input('\nWhich card would you like to play from your hand?\n'))-1]
            table_choice = table[int(
                input('\nWhich card on the table would you like to match with?\n'))-1]

            # ensure card selections are of matching months
            if player.match(hand_choice, table_choice):
                # inherently makes move to sort cards into correct piles if matched
                return

            # else/except if not a valid integer, repeat while loop
            else:
                print(
                    f'\n[ERROR: invalid selection]\nPlease match cards belonging to the same month. {hand_choice.month} is not {table_choice.month}.')
        except ValueError as err:
            print(f'\n[ERROR: {err}] \nPlease enter an integer value.')
        except IndexError as err:
            print(
                f'\n[ERROR: {err}] \nPlease enter values between 1 and {len(player.hand)} for your hand and between 1 and {len(table)} for the table.')
