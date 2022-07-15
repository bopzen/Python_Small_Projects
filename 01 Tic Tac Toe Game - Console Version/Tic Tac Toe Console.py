table = [[" "," "," ",], [" "," "," ",], [" "," "," ",]]
player1_symbol = "X"
player2_symbol = "O"


def print_table():
    print("+-----------+")
    print("| " + " | ".join(table[0]) + " |")
    print("-------------")
    print("| " + " | ".join(table[1]) + " |")
    print("-------------")
    print("| " + " | ".join(table[2]) + " |")
    print("+-----------+")


def welcome():
    print("****************************")
    print("WELCOME TO TIC TAC TOE GAME!")
    print("****************************")
    print_table()


def enter_player1():
    print("\n=======================")
    while True:
        print("PLAYER 1 (X) ")
        print("Enter your coordinates (1 to 3):")
        x1 = int(input("Row: "))
        y1 = int(input("Column: "))
        if x1 < 1 or x1 > 3 or y1 < 1 or y1 > 3:
            print_table()
            print("*** ERROR ***: Coordinates out of range! Please try again!")
            continue
        if table[x1-1][y1-1] == " ":
            break
        else:
            print_table()
            print("*** ERROR ***: The box is not empty! Please try again!")
            continue
    return x1, y1


def enter_player2():
    print("\n=======================")
    while True:
        print("PLAYER 2 (O) ")
        print("Enter your coordinates (1 to 3):")
        x2 = int(input("Row: "))
        y2 = int(input("Column: "))
        if x2 < 1 or x2 > 3 or y2 < 1 or y2 > 3:
            print_table()
            print("*** ERROR ***: Coordinates out of range! Please try again!")
            continue
        if table[x2-1][y2-1] == " ":
            break
        else:
            print_table()
            print("*** ERROR ***: The box is not empty! Please try again!")
            continue
    return x2, y2


def input_table(coordinates, player):
    x = coordinates[0]-1
    y = coordinates[1]-1
    table[x][y] = player


def check_win():
    player1_win = False
    player2_win = False
    end_game = False
    for row in range(len(table)):
        if table[row][0] == table[row][1] == table[row][2] == 'X':
            player1_win = True
            break
        elif table[row][0] == table[row][1] == table[row][2] == 'O':
            player2_win = True
            break
    for column in range(len(table)):
        if table[0][column] == table[1][column] == table[2][column] == 'X':
            player1_win = True
            break
        elif table[0][column] == table[1][column] == table[2][column] == 'O':
            player2_win = True
            break
    if table[0][0] == table[1][1] == table[2][2] == "X":
        player1_win = True
    elif table[0][2] == table[1][1] == table[2][0] == "O":
        player2_win = True
    if player1_win:
        print("*** CONGRATULATIONS ***")
        print("Player 1 WINS the game!")
        end_game = True
    elif player2_win:
        print("*** CONGRATULATIONS ***")
        print("Player 2 WINS the game!")
        end_game = True
    return end_game


def check_full():
    full = True
    for row in range(len(table)):
        for column in range(len(table)):
            if table[row][column] == " ":
                full = False
                break
    if full:
        print("*** END OF GAME ***")
        print("No one wins")
        print("Board is full")
    return full


def another_game():
    while True:
        print("Do you want to play another game? (Y/N)")
        command = input().lower()
        if command == "y" or command == "n":
            break
        else:
            print('*** ERROR ***: Invalid command "Y" or "N" expected. Please try again!')
            continue
    return command

while True:
    table = [[" "," "," ",], [" "," "," ",], [" "," "," ",]]
    player1_symbol = "X"
    player2_symbol = "O"
    welcome()
    while True:
        player1_coordinates = enter_player1()
        input_table(player1_coordinates, player1_symbol)
        print_table()
        end = check_win()
        if end:
            break
        end = check_full()
        if end:
            break
        player2_coordinates = enter_player2()
        input_table(player2_coordinates, player2_symbol)
        print_table()
        end = check_win()
        if end:
            break
        end = check_full()
        if end:
            break
    repeat = another_game()
    if repeat == "y":
        continue
    else:
        break
