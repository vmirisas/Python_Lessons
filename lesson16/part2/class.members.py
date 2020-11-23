class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

molly = Cow(500, 10)
print(type(molly))
print(molly.hunger)



class Person:
    def __init__(self, finstname, surname):
        self.firstname = finstname
        self.surname = surname

person1 = Person("John", "Smith")
print(type(person1))
print(person1.firstname)