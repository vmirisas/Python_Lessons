def float_average(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average


print(f"average = {float_average(1,2,3,4,5,6,7,8,9,10)}")