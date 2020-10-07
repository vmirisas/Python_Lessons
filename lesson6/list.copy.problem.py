list1 = [1, 2, 3]
list2 = list1
list2[0] = 4
print(list1)
print(list2)

print()

# solution1
list3 = [1, 2, 3]
list4 = list3[:]
list4[0] = 4
print(list3)
print(list4)

print()

# solution2
list5 = [1, 2, 3]
list6 = list5.copy()
list6[0] = 4
print(list5)
print(list6)
