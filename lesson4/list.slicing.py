my_list = ["a", "b", "c", "d", "e"]

list1 = my_list[1:4] #returns list[START, END-1]
print(list1)

list2 = my_list[:] #returns a copy of the list
print(list2)

list3 = my_list[2:] #returns list [START, (end of list)]
print(list3)

list4 = my_list[:3] #returns list [(start of the list), END-1]
print(list4)