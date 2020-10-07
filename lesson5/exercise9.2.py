number = int(input("type a number: "))
hidden_number = 4

while number != hidden_number:
    if number <= hidden_number:
        number = int(input("type a greater number: "))
    elif number >= hidden_number:
        number = int(input("type a lesser number: "))
if number == hidden_number:
    print("found it")





