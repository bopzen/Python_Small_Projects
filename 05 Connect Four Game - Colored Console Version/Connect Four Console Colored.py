import pyfiglet
from colorama import Fore, Back, Style, init


def welcome():
    welcome_message = pyfiglet.figlet_format('*  Connect Four  *')
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + welcome_message)


def create_table(rows, columns):
    table = []
    for i in range(rows):
        table.append([])
        for j in range(columns):
            table[i].append('0')
    return table


def print_table(table):
    print()
    for row in table:
        for element in row:
            if element == '1':
                print(Fore.LIGHTRED_EX + Style.BRIGHT + element, end=' ')
            elif element == '2':
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + element, end=' ')
            else:
                print(Fore.YELLOW + element, end=' ')
        print()


def take_turn(player):
    try:
        col = int(input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + f"\n{player}, please choose your column: ")) - 1
    except ValueError:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + f'Enter numbers only!')
        return take_turn(player)
    for row in range(len(current_table)-1, -1, -1):
        try:
            if current_table[row][col] == '0':
                current_table[row][col] = player[-1]
                break
        except IndexError:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + f'Enter valid value between 1 and {table_cols}!')
            return take_turn(player)
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + 'No more spaces left')
        return take_turn(player)


def check_draw():
    for row in current_table:
        if '0' in row:
            return False
    return True


def check_winner(player):
    for row in range(table_rows):
        for col in range(table_cols):
            if current_table[row][col] == player[-1]:
                for coordinates in directions:
                    check_row, check_col = row, col
                    for _ in range(3):
                        check_row += coordinates[0]
                        check_col += coordinates[1]
                        if not 0 <= check_row < table_rows or not 0 <= check_col < table_cols:
                            break
                        if current_table[check_row][check_col] != player[-1]:
                            break
                    else:
                        return True
    return False


def play_another_game():
    another_game = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Do you want another game Y/N: ')
    if another_game.upper() == 'Y':
        return True
    elif another_game.upper() == 'N':
        return False
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + 'Enter Y or N!')
        return play_another_game()


table_rows = 6
table_cols = 7
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]
init(autoreset=True)

while True:
    players = ['Player1', 'Player2']
    current_table = create_table(table_rows, table_cols)
    welcome()
    print_table(current_table)

    while True:
        current_player = players[0]
        take_turn(current_player)
        print_table(current_table)
        if check_draw():
            print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f"It's a draw. No one wins!")
            break
        if check_winner(current_player):
            print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'Winner is {current_player}')
            break
        players[0], players[1] = players[1], players[0]

    if play_another_game():
        continue
    else:
        break


