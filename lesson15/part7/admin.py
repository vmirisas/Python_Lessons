import json

try:
    with open("users.json")as f:
        users = json.load(f)
except FileNotFoundError:
    users = []

while True:
    print("1 - new user")
    print("2 - exit")
    choice = int(input("Type a number: "))

    if choice == 1:
        user = {}
        user["full_name"] = input("Type the users full name: ")
        user["username"] = input("Type the users username: ")
        user["password"] = input("Type the users password: ")
        user["role"] = input("Type the users role(admin, user): ")
        users.append(user)
    elif choice == 2:
        with open("users.json", "w")as f:
            json.dump(users, f)
        break
