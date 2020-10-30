def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


my_list = [5, 4, 8, 13, 20, 57, 9, 12, 4, 87]
print(my_list)
insertion_sort(my_list)
print(my_list)
