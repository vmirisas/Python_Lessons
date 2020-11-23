class Dog:
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.mood = 3

    def eat(self):
        self.mood += 1

    def walk(self):
        self.mood += 1

    def bark(self):
        if self.mood > 5:
            print("Woof woof woof")
        else:
            print("Woof")



dogo = Dog("Terry", 10, "Labrador")

dogo.bark()

dogo.walk()
dogo.bark()

dogo.walk()
dogo.bark()

dogo.eat()
dogo.bark()