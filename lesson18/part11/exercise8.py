from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class HimalayanCat(Cat):
    def make_sound(self):
        super().make_sound()
        print(f"Miouw Miouw")


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")


class Doberman(Dog):
    pass


class KingDoberman(Doberman):
    def make_sound(self):
        super().make_sound()
        print(f"WOOOOAAAF")


psipsina = Cat()
gataros = HimalayanCat()
boubis = Dog()
babis = Doberman()
bobos = KingDoberman()

psipsina.make_sound()
gataros.make_sound()
boubis.make_sound()
babis.make_sound()
bobos.make_sound()
