from math import sqrt


class Circle:
    def __init__(self, c):
        self.c = c

    def __str__(self):
        return f"x^2 + y^2 = {self.c}^2"

    def __eq__(self, other):
        return self.c == other.c

    def __lt__(self, other):
        return self.c < other.c

    def __call__(self, x, y=None):
        if y is None:
            if isinstance(x, (int, float)):
                if x < abs(self.c):
                    return (x, sqrt(self.c ** 2 - x ** 2)), (x, -sqrt(self.c ** 2 - x ** 2))
                elif abs(x) == self.c:
                    return (x, 0)
                else:
                    return None
        else:
            if isinstance(x, (int, float)):
                if x ** 2 + y ** 2 < self.c ** 2:
                    print(f"({x}, {y}) is inside the circle")
                elif x ** 2 + y ** 2 == self.c ** 2:
                    print(f"({x}, {y}) is on the circle")
                else:
                    print(f"({x}, {y}) is out of the circle")


circle = Circle(5)
print(circle(3))
print(circle(5))
print(circle(7))
circle(1, 1)
circle(5, 0)
circle(5, 9)
