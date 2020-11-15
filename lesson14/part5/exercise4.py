table1 = [
    [3, 7, 9, 6, 1],
    [4, 9, 2, 5, 8],
    [7, 8, 3, 1, 6],
    [5, 7, 3, 9, 2],
    [1, 9, 6, 7, 4]
]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                #print(array)
    return array


def sort_by_rows(table):
    for row in table:
        print(f'===== ROW-{table.index(row) + 1} ======')
        bubble_sort(row)

    return table


def sort_by_cols(table):
    for j in range(len(table)):
        col = [row[j] for row in table]
        bubble_sort(col)
        i = 0
        for row in table:
            row[j] = col[i]
            i += 1
    for row in table:
        print(row)




#print(sort_by_rows(table1))
sort_by_cols(table1)
#print(table1)
