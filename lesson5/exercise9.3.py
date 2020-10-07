number = int(input("type a number: "))
hidden_number = 4
tries = 0
max_tries = 5

while True:

    tries += 1
    print("you have " + str(max_tries - tries) + " tries")
    if tries == max_tries:
        print("you lose the game")
        break

    if number > hidden_number:
        print("try a lesser one")
    elif number < hidden_number:
        print("try a greater one")
    else:
        print("you've found it!")
        break
    number = int(input("type a number: "))
