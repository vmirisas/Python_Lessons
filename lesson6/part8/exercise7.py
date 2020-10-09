card_matrix = [1, 4, 3, 2, 4, 1, 3, 2]
N = 8

state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]
# states : closed, open, temp_open

active_game = True
found = 0
tries = 0
while active_game:
    tries += 1
    # open first card
    first_position = int(input("Type first position(0 - (N-1) and closed: "))
    while (first_position < 0 or first_position >= N) or state[first_position] == "open":
        print("Error!")
        first_position = int(input("Type first position(0 - (N-1) and closed: "))

    # open second card
    second_position = int(input("Type second position(0 - (N-1) and closed: "))
    while (second_position < 0 or second_position >= N) or state[second_position] == "open" or second_position == first_position:
        print("Error!")
        second_position = int(input("Type first position(0 - (N-1) and closed: "))

    # change state: both temp_open
    state[first_position] = "temp_open"
    state[second_position] = "temp_open"

    # print current state
    print("")
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(card_matrix[position], end="")
        else:
            print(card_matrix[position], end="")
    print("")

    # check if same then open, else closed
    if card_matrix[first_position] == card_matrix[second_position]:
        state[first_position]= "open"
        state[second_position] = "open"
        print("Success!")
        found += 2
        if found == N:
            print("Game Finished, well done!, You did: " + str(tries) + " tries")
            active_game = False
    else:
        state[first_position] = "closed"
        state[second_position] = "closed"
        print("Fail")

    print("")
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(card_matrix[position], end="")
        else:
            print(card_matrix[position], end="")
    print("")