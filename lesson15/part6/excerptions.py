import json

try:
    with open("reminders.txt")as f:
        reminders = json.load(f)
except FileNotFoundError:
    reminders = []