numbers = []
number = int(input("type a number N, 3>N>20: "))
while number < 3 or number > 20:
    number = int(input("type a number N, 3>N>20: "))
for i in range(0, number):
    if i == 0:
        numbers.append(int(input("type the " + str(i + 1) + "st number: ")))
    elif i == 1:
        numbers.append(int(input("type the " + str(i + 1) + "nd number: ")))
    else:
        numbers.append(int(input("type the " + str(i + 1) + "th number: ")))
print(numbers)
numbers.sort()
print(numbers)
