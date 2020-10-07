number_list = []

for i in range(10):
    n = int(input("type the " + str(i) + " number:"))
    while n < 10 or n > 20:
        n = int(input("type the " + str(i) + " number:"))
    number_list.append(n)

print(number_list)
my_tuple = tuple(number_list)
print(my_tuple)

squares_list = []
for i in range(10):
    squares_list.append(number_list[i]**2)
print(squares_list)
squares_list.sort()
squares_tuple = tuple(squares_list)
print(squares_tuple)