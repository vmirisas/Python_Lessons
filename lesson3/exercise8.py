from random import randrange

a1 = randrange(1, 7)
a2 = randrange(1, 7)
b1 = randrange(1, 7)
b2 = randrange(1, 7)

a_sum = a1 + a2
b_sum = b1 + b2
print("number1 players rolls: " + str(a1) +  " + " + str(a2) + " = " + str(a_sum))
print("number2 players rolls: " + str(b1) +" + " + str(b2) + " = " + str(b_sum))

if a_sum > b_sum:
    print("player number 1 goes first")
elif a_sum < b_sum:
    print("player number 2 goes first")
else:
    print("the players must reroll")