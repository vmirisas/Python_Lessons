from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

turn = 0
score = [0, 0]  # player, computer
history = []

while True:
    turn += 1
    print("Turn " + str(turn))

    player_input = input("rock, paper, scissors: ")
    while player_input not in ["rock", "paper", "scissors"]:
        print("wrong input")
        player_input = input("rock, paper, scissors: ")

    availiable_choices = ("rock", "paper", "scissors")

    computer_choice = availiable_choices[randrange(3)]

    if player_input == "rock":
        if computer_choice == "paper":
            winner = "computer"
        elif computer_choice == "scissors":
            winner = "player"
        else:
            winner = "draw"
    elif player_input == "paper":
        if computer_choice == "rock":
            winner = "computer"
        elif computer_choice == "scissors":
            winner = "player"
        else:
            winner = "draw"
    else:
        if computer_choice == "rock":
            winner = "computer"
        elif computer_choice == "paper":
            winner = "player"
        else:
            winner = "draw"

    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1

    history.append("Turn " + str(turn) + ": Player: " + player_input + ", Computer: " + computer_choice + ", Score: " + str(score[0]) + "-" + str(score[1]))

    print("Computer picks: " + computer_choice)
    print("winner of this turn: " + winner)
    print("Computer: " + str(score[1]) + "  " + "Player: " + str(score[0]))
    print("===========\n")

    if score[0] == 3:
        print("the winner is the player")
        print("")
        for history_item in history:
            print(history_item)
        break
    elif score[1] == 3:
        print("the winner is the computer")
        print("")
        for history_item in history:
            print(history_item)
        break
