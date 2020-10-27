pi = 3.14159265359

def triangle_area(base, hight):
    return (base + hight) / 2


def square_perimeter(edge):
    return 4 * edge


def square_area(edge):
    return edge ** 2


def circle_perimeter(radius):
    return 2 * pi * radius


def circle_area(radius):
    return pi * radius ** 2


print(triangle_area(4,5))
print(square_perimeter(4))
print(square_area(5))
print(circle_perimeter(2))
print(circle_area(4))
