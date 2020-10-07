N = int(input("type the number of lines"))
table = []

for i in range(0, N):
    for j in range(0, N-1-i):
        print(" ", end=" ")
    for j in range(0, 2*i+1):
        print("*", end=" ")

    print()
