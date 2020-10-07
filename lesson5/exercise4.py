numbers = [1, 2, 3, 4, 15445215, 6, 7, 8, 9, 10]
max = numbers[0]
counter = 1
while counter < len(numbers):
    if numbers[counter] > max:
        max = numbers[counter]
    counter += 1

print(max)
