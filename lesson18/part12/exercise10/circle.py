from geometric_object_interface import GeometricObjectInterface
from resizable import Resizable
from math import pi


class Circle(GeometricObjectInterface):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class CircleResizable(Circle, Resizable):
    def __init__(self, radius):
        Circle.__init__(self, radius)

    def resize(self, param):
        self.radius =  self.radius * param