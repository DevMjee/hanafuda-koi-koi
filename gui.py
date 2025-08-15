"""Module for common functions to print cards and display game neatly"""


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


def display_contents(contents, msg):
    """function to format lists with subheadings consistently"""
    print('\n###', str(msg).upper(), '###')
    print_choices(contents)


def validate_input(msg, highest):
    """function to ensure only valid integer inputs throughout"""
    while True:
        try:
            # - 1 to make usable for indexing
            choice = int(input(f'\n{msg}\n')) - 1
            # even if integer, confirm within correct range
            if choice in range(highest):
                return choice
            else:
                print(msg[1000])  # force index error if out of range

        except ValueError as err:  # if not integer
            print(f'\n[ERROR: {err}] \nPlease enter an integer value')

        except IndexError as err:  # if out of range
            print(
                f'[ERROR: {err}] \nPlease enter a valid integer choice between 1 and {highest}.')


def print_win(card_set, special=None):
    """function for printing sets won consistently"""
    if special:
        print(f'\n{special.upper()} {card_set.upper()} SET WON!')
    else:
        print(f'\n{card_set.upper()} SET WON!')
