from abc import ABC, abstractmethod


class GeometricObjectInterface(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
