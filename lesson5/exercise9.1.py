number = int(input("type a number: "))
hidden_number = 4
while hidden_number != number:
    number = int(input("wrong number, try again: "))
    if hidden_number == number:
        print("found it")
        break
