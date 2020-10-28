from random import seed
from random import randrange
from datetime import datetime


def player1_pick():
    # global deck
    player1.add(deck.pop())


def player2_pick():
    # global deck
    player2.add(deck.pop())


def play():
    print("let the game begin!")
    for card in range(len(deck)):
        if randrange(2) == 0:
            player1_pick()
        else:
            player2_pick()
    print(f"player's 1 cards:  {len(player1)} cards")
    print(f"player's 2 cards:  {len(player2)} cards")

    if len(player1) > len(player2):
        print("Player1 wins")
    elif len(player1) == len(player2):
        print("Draw")
    else:
        print("player2 wins!")

seed(datetime.now())

numbers = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
kind = {"spades", "hearts", "clubs", "diamonds"}

deck = {(number, k) for number in numbers for k in kind}

player1 = set()
player2 = set()

print(len(deck))
play()