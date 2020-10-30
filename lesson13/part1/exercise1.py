def f(x, y, z):
    function = 2 * (x ** 3) + 3 * ((x ** 2) * y) + ((y ** 2) * z) + 1
    return print(function)


f(5, 2, 3)
f(x=5, y=2, z=3)
f(5, y=2, z=3)
f(5,2,z=3)
f(5, z=3, y=2)


