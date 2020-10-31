# Selection Sort
def selection_sort(array):
    for i in range(0, len(array)):
        pos = i
        for j in range(i + 1, len(array)):
            if array[j] < array[pos]:
                pos = j
        array[i], array[pos] = array[pos], array[i]
        print(array)
    return array


print(selection_sort([5, 4, 3, 1, 2]))
