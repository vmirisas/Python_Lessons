while True:
    string = input("type your name: ")
    string = string.strip()
    if string.isalpha():
        name = string.capitalize()
        print(f"Name entered: {name}")
        break
    else:
        print("type only characters!")

while True:
    string = input("type your surname: ")
    string = string.strip()
    if string.isalpha():
        surname = string.capitalize()
        print(f"Surname entered: {surname}")
        break
    else:
        print("type only characters!")

print(f"+{28 * '-'}+")
print(f"|{(name + ' ' + surname).center(28)}|")
print(f"+{28 * '-'}+")
