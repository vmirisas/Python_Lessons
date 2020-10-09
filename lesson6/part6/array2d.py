my_list = [
    [1, 2, 3],
    [4, 5, 6]
]
print(my_list)

array = []
rows = int(input("give number of rows: "))
columns = int(input("give number of columns: "))
for i in range(rows):
    array.append([])
    for j in range(columns):
        element = int(input("Type " + str(i) + "," + str(j) + " element of the matrix: "))
        array[i].append(element)
print(array)