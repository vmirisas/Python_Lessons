from random import seed
from datetime import datetime

# globals


numbers = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
kind = {"spades", "hearts", "clubs", "diamonds"}
deck = {(number, k) for number in numbers for k in kind}


# functions

def hand_value(hand):
    s = 0
    ace = False
    for card in hand:
        n = card[0]
        if n == "jack" or n == "queen" or n == "king":
            s += 10
        elif n == "ace":
            ace = True
            s += 1
        else:
            s += n
    if ace:
        if s + 10 <= 21:
            s += 10
    return s


def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())
    while True:
        print(hand)
        choice = input("H-Hit or S-Stand: ")
        if choice == "H":
            hand.add(deck.pop())
            value = hand_value(hand)
            if value >= 21:
                return value
        elif choice == "S":
            return hand_value(hand)


def computer(value_player, hand):
    hand.add(deck.pop())
    hand.add(deck.pop())
    while True:
        value = hand_value(hand)
        if value >= 21:
            return value
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())


# main

def main():
    seed(datetime.now())
    rounds = 1
    score = [0, 0]
    while True:
        print("=" * 15)
        print(f"Round {str(rounds)}")
        print("=" * 15)

        player_hand = set()
        player_value = player(player_hand)

        print(f"{player_hand} with value: {player_value}")
        if player_value == 21:
            print("You win!")
            result = "player"
        elif player_value > 21:
            print("You lose")
            result = "computer"
        else:
            print("Computers turn")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)
            print(f"{computer_hand} with value: {computer_value}")
            if computer_value > 21:
                print("You win!")
                result = "player"

            else:
                print("you lose")
                result = "computer"

        if result == "player":
            score[0] += 1
        else:
            score[1] += 1

        print(f"Score: Player: {score[0]} - Computer: {score[1]}")
        choice = input("wanna play again? : Y-Yes, N-No: ")
        if choice == "N":
            break


main()
