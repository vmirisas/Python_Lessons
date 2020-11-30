from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


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

    def __str__(self):
        return f"{self.point_a} - {self.point_b}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.length() == other
        elif isinstance(other, Line):
            return self.length() == other.length()

    def __lt__(self, other):
        if isinstance(other, int):
            return self.length() < other
        elif isinstance(other, Line):
            return self.length() < other.length()

    def __le__(self, other):
        if isinstance(other, int):
            return self.length() <= other
        elif isinstance(other, Line):
            return self.length() <= other.length()


l1 = Line(Point(1, 1), Point(4, 5))
l2 = Line(Point(1, 1), Point(4, 8))

print(l1 < l2)
print(l1 > l2)
print(l1 <= l2)
print(l1 >= l2)
print(l1 == l2)
print(l1 != l2)
print(l1 == 5)
