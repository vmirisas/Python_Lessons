class Animal:
    def make_sound(self):
        print("----")


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


sir = Animal()
psipsina = Cat()
gataros = HimalayanCat()
boubis = Dog()
babis = Doberman()
bobos = KingDoberman()

sir.make_sound()
psipsina.make_sound()
gataros.make_sound()
boubis.make_sound()
babis.make_sound()
bobos.make_sound()
