# tic tak toe
# globals
from random import randrange, seed
from datetime import datetime

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


# functions
def print_board():
    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2")


def check_row(row):
    return board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " "


def check_col(col):
    return board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " "


def check_diagonals():
    return (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ") or (
            board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ")


def computer_moves(level):
    def danger_sequence(sequence):
        xs = 0
        empty = None
        for sq in sequence:
            if board[sq[0]][sq[1]] == "x":
                xs += 1
            elif board[sq[0]][sq[1]] == " ":
                empty = sq

        if xs == 2 and empty is not None:
            return empty
        return None

    def danger():
        for i in range(3):
            row = [(i, j) for j in range(3)]
            sq = danger_sequence(row)
            if sq is not None:
                return sq
        for j in range(3):
            col = [(i, j) for j in range(3)]
            sq = danger_sequence(col)
            if sq is not None:
                return sq

        sq = danger_sequence([(0, 0), (1, 1), (2, 2)])
        if sq is not None:
            return sq

        sq = danger_sequence([(2, 0), (1, 1), (0, 2)])
        if sq is not None:
            return sq

    squares = []
    if level == 1:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    squares.append((i, j))
        return squares[randrange(len(squares))]
    else:  # hard
        sq = danger()
        if sq is not None:
            return sq
        elif board[1][1] == " ":
            return (1, 1)
        else:
            corner_squares = [(0, 0), (0, 2), (2, 0), (2, 2)]
            empty_squares = []
            for sq in corner_squares:
                if board[sq[0]][sq[1]] == " ":
                    empty_squares += [sq]
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]

            middle_squares = [(0, 1), (1, 0), (1, 2), (2, 1)]
            empty_squares = []
            for sq in middle_squares:
                if board[sq[0]][sq[1]] == " ":
                    empty_squares += [sq]
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]


def main():
    seed(datetime.now())

    level = int(input("choose level of difficulty (1-easy, 2-hard): "))

    player = "o"

    for i in range(9):  # 9 moves in total
        print_board()
        # choose the next player to play
        if player == "x":
            player = "o"
        else:
            player = "x"

        # user input

        while player == "x":
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
        if player == "o":
            sq = computer_moves(level)
            board[sq[0]][sq[1]] = "o"

        # check winner
        winner = False
        for i in range(3):
            if check_row(i):
                winner = player
                break
            elif check_col(i):
                winner = player
                break
        if not winner:
            if check_diagonals():
                winner = player

        if winner:
            print_board()
            print("Player " + player + " wins!")
            break
    else:
        print_board()
        print("Draw")


# main
main()
