my_set = {number for number in range(3)}

my_set1 = {number for number in range(10) if number % 2 == 0}

my_set2 = {number if number % 2 == 0 else number / 2 for number in range(10)}

"""
my_set3 = set()
for i in range(2):
    for j in range(3):
        my_set3.add(i,j)
"""
my_set3 = {(i, j) for i in range(2)
           for j in range(3)}

"""
my_set3 = set()
for i in range(6):
    if i%2==0:
    for j in range(6,10):
        if j%2 ==1:
            my_set4.add(i,j)
"""

my_set4 = {(i, j) for i in range(6) if i % 2 == 0
           for j in range(6, 10) if j % 2 == 1}
print(my_set)
print(my_set1)
print(my_set2)
print(my_set3)
print(my_set4)
