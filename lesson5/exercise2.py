counter= 1
sum_input = 0
while counter <= 10:
    user_input = input("Type " + str(counter) + "th number: ")
    counter += 1
    sum_input += int(user_input)
print("the sum of the  10 numbers is: " + str(sum_input))