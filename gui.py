"""Module for common functions to print cards and display game neatly"""


def display_contents(contents, msg):
    print('\n###', str(msg).upper(), '###')
    print_choices(contents)


def print_choices(contents):
    """function to print and display cards neatly with spacing"""
    if contents:

        # print list of cards two at a time
        for index, choice in enumerate(contents, start=1):
            if index % 2 == 0:
                continue
            else:
                hand_print = f'[{index}] - {choice}'
                hand_print = hand_print.ljust(40)
                # only pass if another choice to display exists
                if choice != contents[-1]:
                    hand_print += f'    [{index+1}] - {contents[index]}'
            print(hand_print)

    else:
        print('Empty!')


def validate_between_two(player, msg):
    while True:
        try:
            choice = int(input(f'\n{msg}\n'))
            if choice in (1, 2):
                return choice
            else:
                print(player.hand[9])  # force index error if out of range(2)

        except ValueError as err:
            print(f'\n[ERROR: {err}] \nPlease enter an integer value')

        except IndexError as err:
            print(
                f'[ERROR: {err}] \nPlease enter a valid choice: either 1 or 2')


def validate_input(player, table, draw=False, skip=False):
    """function to check valid integer inputs for working controls"""
    while True:
        try:  # try to accept integer inputs and compare the card months
            if draw:  # during turn draw
                hand_choice = draw
            else:  # during turn play
                hand_choice = player.hand[int(
                    input('\nWhich card would you like to play from your hand?\n'))-1]
            if skip:  # don't pick from table if putting down card for turn
                return hand_choice
            else:
                table_choice = table[int(
                    input('\nWhich card on the table would you like to match with?\n'))-1]

            return hand_choice, table_choice

        except ValueError as err:
            print(f'\n[ERROR: {err}] \nPlease enter an integer value.')
        except IndexError as err:
            print(
                f'\n[ERROR: {err}] \nPlease enter values between 1 and {len(player.hand)} for your hand and between 1 and {len(table)} for the table.')
