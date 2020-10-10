# tic tak toe
# this code has many architectural mistakes, its an exercise of simple programming
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "x"

for i in range(9):  # 9 moves in total

    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2")

    # choose the next player to play
    if player == "x":
        player = "o"
    else:
        player = "x"

    # user input

    while True:
        print("Player " + player + " plays")
        row = int(input("Type row: "))
        column = int(input("Type column: "))
        if row < 0 or row > 2:
            print("Row out of bounds (0-2)")
            continue
        elif column < 0 or column > 2:
            print("Column out of bounds (0-2)")
            continue
        elif board[row][column] != " ":
            print("position already filled, pick another one")
            continue
        else:
            board[row][column] = player
            break

    winner = False
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
        winner = player
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ":
        winner = player
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ":
        winner = player
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != " ":
        winner = player
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ":
        winner = player
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ":
        winner = player
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        winner = player
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        winner = player

    if winner:
        print("+---+---+---+")
        print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
        print("+---+---+---+")
        print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
        print("+---+---+---+")
        print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
        print("+---+---+---+")
        print("Player " + player + " wins!")
        break


else:
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("Draw")
