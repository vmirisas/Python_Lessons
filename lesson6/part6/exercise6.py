matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matrix)


matrix.insert(0, [0, 0, 0, 0])

for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print("")

print()

for row in matrix:
    row.append(1)

for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print("")