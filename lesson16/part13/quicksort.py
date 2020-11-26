from random import randrange


def quick_sort(array):
    length = len(array)

    if length <= 1:
        return array
    else:
        pivot = array.pop()

    items_greater = []
    items_lower = []

    for item in array:
        if item > pivot:
            items_greater.append(item)
            # print(items_greater)
        else:
            items_lower.append(item)
            # print(items_lower)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


a = [randrange(100) for _ in range(10)]
print(quick_sort(a))
