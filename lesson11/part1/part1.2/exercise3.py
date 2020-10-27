def input_integer():
    int_input = input("Type a number: ").strip()
    while int_input.isdigit() == False:
        print("Wrong type of input!")
        int_input = input("Type an integer: ")
    return int(int_input)


print(input_integer())
