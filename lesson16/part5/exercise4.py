class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


def f(x):
    return x ** 2


points = []

for x in range(1, 10 + 1):
    p = Point(x, f(x))
    points.append(p)

for point in points:
    print(f"({point.get_x()},{point.get_y()})")

# =========================same thing, different way=============================

points2 = [Point(i, f(i)) for i in range(11)]
for b in points2:
    print(f"({b.get_x()},{b.get_y()})")



print(points2[1].get_x())
points2[1].set_x(12)
points2[1].set_y(f(points2[1].get_x()))
print(f"{points2[1].get_x()}, {points2[1].get_y()}")
