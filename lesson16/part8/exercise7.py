from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def print(self):
        print(f"({self.x}, {self.y})")


class Line:
    def __init__(self, point_a=None, point_b=None):
        if point_a is None:
            self.point_a = Point(0, 0)
        else:
            self.point_a = point_a

        if point_b is None:
            self.point_b = Point(0, 0)
        else:
            self.point_b = point_b

    def set_point_a(self, point_a):
        self.point_a = point_a

    def set_point_b(self, point_b):
        self.point_b = point_b

    def length(self):
        return sqrt((self.point_a.x - self.point_b.x) ** 2 + (self.point_a.y - self.point_b.y) ** 2)

    def print(self):
        self.point_a.print()
        self.point_b.print()


line1 = Line()
line1.print()
line1.set_point_a(Point(1, 1))
line1.set_point_b(Point(4, 5))
line1.print()
print(line1.length())
