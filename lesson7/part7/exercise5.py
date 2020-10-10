# POKER

from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 52
deck = set()
numbers = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
kind = {"spades", "hearts", "clubs", "diamonds"}


deck = {(number, k) for number in numbers
           for k in kind}
print(len(deck))

player1 = set()
player2 = set()

list_deck = list(deck)
for i in range(5):
    pos1 = randrange(len(list_deck))
    player1.add(list_deck.pop(pos1))
    pos2 = randrange(len(list_deck))
    player2.add(list_deck.pop(pos2))

print(player1)
print(player2)

# Four of Aces
# player1
print(player1)
counter = 0
for card in player1:
    if card[0] == "ace":
        counter += 1
if counter == 4:
    print("Player 1 has Four of Aces")

# player2
counter = 0
for card in player2:
    if card[0] == "ace":
        counter += 1
if counter == 4:
    print("Player 2 has Four of Aces")

#player1

hand_numbers = []
for card in player1:
    if card[0] == "ace":
        hand_numbers.append(1)
    elif card[0] == "jack":
        hand_numbers.append(11)
    elif card[0] == "queen":
        hand_numbers.append(12)
    elif card[0] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[0])

hand_numbers.sort()
print(hand_numbers)

for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos+1] -1:
        break
else:
    print("player 1 has full house")

# player2
hand_numbers = []
for card in player2:
    if card[0] == "ace":
        hand_numbers.append(1)
    elif card[0] == "jack":
        hand_numbers.append(11)
    elif card[0] == "queen":
        hand_numbers.append(12)
    elif card[0] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[0])

hand_numbers.sort()
print(hand_numbers)

for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos+1] -1:
        break
else:
    print("player 2 has full house")