number = int(input("type a number: "))
while number<=0 or number>9:
    number = int(input("type a number between 0 and 9: "))

print(str(number) + " is the number you entered")