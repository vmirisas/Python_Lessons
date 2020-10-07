hidden_number = 5
counter = 0
max_guesses = 10
number = int(input("type a number: "))

"""if number == hidden_number:
    print("you win!")

while number != hidden_number:
    counter += 1
    if counter == max_guesses:
        print("you lose the game")
        break

    if hidden_number > number:
        print("type a grater one")
    elif hidden_number < number:
        print("type a smaller one ")

    number = int(input("type a number: "))
    if number == hidden_number:
        print("you win!")
"""


while True:
    counter += 1
    if counter == max_guesses:
        print("you lose the game")
        break

    if hidden_number > number:
        print("type a grater one")
    elif hidden_number < number:
        print("type a smaller one ")
    else:
        print("you win!")
        break

    number = int(input("type a number: "))
