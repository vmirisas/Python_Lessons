from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

turn = 0
score = [0, 0]  # player, computer
history = []

while True:
    turn += 1
    print(f"Turn  {turn}")

    player_input_str = input("rock, paper, scissors: ")
    while player_input_str not in ["rock", "paper", "scissors"]:
        print("wrong input")
        player_input_str = input("rock, paper, scissors: ")

    if player_input_str == "rock":
        player_input_int = 0
    elif player_input_str == "scissors":
        player_input_int = 1
    else:
        player_input_int = 2

    computer_choice_int = randrange(3)
    if computer_choice_int == 0:
        computer_choice_str = "rock"
    elif player_input_str == 1:
        computer_choice_str = "scissors"
    else:
        computer_choice_str = "paper"

    diff = player_input_int - computer_choice_int

    if diff == -1 or diff == 2:
        winner = "player"
    elif diff == 1 or diff == -2:
        winner = "computer"
    else:
        winner = "none"
    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1

    history.append("Turn " + str(
        turn) + ": Player: " + player_input_str + ", Computer: " + computer_choice_str + ", Score: " + str(
        score[0]) + "-" + str(score[1]))
    history.append(
        f"Turn {turn}: Player: {player_input_int}, Computer: {computer_choice_int} , Score: {score[0]} - {score[1]}")

    print("Computer picks: " + computer_choice_str)
    print("winner of this turn: " + winner)
    print(f"Computer: {score[1]} ,Player: {score[0]}")
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
