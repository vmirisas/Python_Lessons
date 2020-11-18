import json

try:
    with open("reminders.txt")as f:
        reminders = json.load(f)
except FileNotFoundError:
    reminders = []

while True:
    print("1 - add reminder")
    print("2 - remove reminder")
    print("3 - print reminder")
    print("4 - exit")
    choice = int(input("Choose a number (1-4): "))

    if choice == 1:
        reminder = input("Type the new reminder: ")
        reminders.append(reminder)
        with open("reminders.json", "w")as f:
            json.dump(reminders, f)
    elif choice == 2:
        reminder_index = int(input("Type the index of the reminder: "))
        reminders.pop(reminder_index)
        with open("reminders.json","w")as f:
            json.dump(reminders, f)
    elif choice == 3:
        for i in range(len(reminders)):
            print(f"{i} : {reminders[i]}")
    elif choice == 4:
        break

