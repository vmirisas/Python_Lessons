x = int(input("type an integer for x: "))
y = int(input("type an integer for y: "))
z = int(input("type an integer for z: "))

max_input = x
if y > max_input:
    max_input = y
if z > max_input:
    max_input = z

print(max_input)

"""if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
else:
    print(z)
"""