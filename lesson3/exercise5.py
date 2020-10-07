x = int(input("type an integer for x: "))
y = int(input("type an integer for y: "))
z = int(input("type an integer for z: "))

if x >= y and x >= z:
    print(x)

if y >= x and y >= z:
    print(y)

if z >= x and z >= y:
    print(z)