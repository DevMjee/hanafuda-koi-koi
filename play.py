"""Module to play koi-koi with hanafuda"""
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
        try:  # try to accept integer inputs and compare the card months
            hand_choice = player.hand[int(
                input('Which card would you like to play?\n'))-1]
            table_choice = table[int(
                input('Which card on the table would you like to match with?\n'))-1]

            # ensure card selections are of matching months
            if player.match(hand_choice, table_choice):
                break
            else:  # except if not an integer repeat while loop
                print(
                    f'Please match cards belonging to the same month. {hand_choice.month} is not {table_choice.month}.')
        except ValueError:
            print(
                f'Please enter two valid indices between 1 and {len(player.hand)} for your hand and between 1 and {len(table)} for the table.')


def play_game(player_1, player_2):
    """function to simulate games between different players"""
    while True:
        for player in (player_1, player_2):
            make_move(player, koi_koi.table.contents)
            new_card = koi_koi.deck.contents.pop()
            koi_koi.deck.remove_cards([new_card])
            player.draw(new_card, koi_koi.table.contents)
            for card in player.collected:
                print(card)
            if input('continue?') == 'no':
                break


if __name__ == '__main__':
    play_game(koi_koi.player_1, koi_koi.player_2)
