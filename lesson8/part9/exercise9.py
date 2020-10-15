from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

player_input = input("rock, paper, scissors: ")
while player_input not in ["rock", "paper", "scissors"]:
    print("wrong input")
    player_input = input("rock, paper, scissors: ")

availiable_choices = ("rock", "paper", "scissor")

computer_choice = availiable_choices[randrange(3)]

winner = ""
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

print("Computer: " + computer_choice + "  " + "Player: " + player_input)
print(winner)
