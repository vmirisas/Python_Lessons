while True:
    string = input("Give an integer: ")
    if string.isdigit():
        number = int(string)
        print(f"Number entered: {number}")
        break
    else:
        print("type an integer!")