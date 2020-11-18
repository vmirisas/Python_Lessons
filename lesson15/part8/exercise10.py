# merge sort
from random import randrange


def merge_sort(array):
    def merge(array, start, finish):
        c = []
        middle = (start + finish) // 2
        i = start
        n = middle
        j = middle + 1
        m = finish

        while i <= n and j <= m:
            if array[i] < array[j]:
                c += [array[i]]
                i += 1
            else:
                c += [array[j]]
                j += 1
        if i == n + 1:
            c += array[j:m + 1]
        else:
            c += array[i:n + 1]

        i = start
        j = 0
        while i <= finish:
            array[i] = c[j]
            i += 1
            j += 1

    def merge_sort_rec(array, start, finish):
        if start == finish:
            return
        elif start == finish - 1:
            if array[start] > array[finish]:
                array[start], array[finish] = array[finish], array[start]
        else:

            middle = (start + finish) // 2

            merge_sort_rec(array, start, middle)
            merge_sort_rec(array, middle + 1, finish)
            merge(array, start, finish)


    merge_sort_rec(array, 0, len(array)-1)

ar = [randrange(100) for i in range(10)]
print(ar)
merge_sort(ar)
print(ar)
