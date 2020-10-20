x = [1, 2]
print(f"x:{id(x)}, x[0]:{id(x[0])}, x[1]:{id(x[1])}")
y = x
print(f"y:{id(y)}, y[0]:{id(y[0])}, y[1]:{id(y[1])}")
y = x.copy()  # y=x[:]
print(f"y:{id(y)}, y[0]:{id(y[0])}, y[1]:{id(y[1])}")
y[1] = 3
print(f"x:{id(x)}, x[0]:{id(x[0])}, x[1]:{id(x[1])}")
print(f"y:{id(y)}, y[0]:{id(y[0])}, y[1]:{id(y[1])}")

list1 = [1,2]
list2 = [1,2]
print(id(list1))
print(id(list2))