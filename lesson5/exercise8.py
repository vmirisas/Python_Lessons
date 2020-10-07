n = int(input("type a number 3 >= N >= 20: "))
input_list = []

while n < 3 or n > 20:
    n = int(input("type a number 3 >= N >= 20: "))

for number in range(0,n):
    input_list.append(int(input("type the " + str(number+1) + "th number: ")))
input_list.sort()
print(input_list)