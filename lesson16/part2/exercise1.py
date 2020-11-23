class Dog:
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed


dog1 = Dog("Piko", 10, "Terrier")
dog2 = Dog("Lassie", 30, "Colley")


print(f"the dog named {dog1.name}, weighs {dog1.weight} and is a {dog1.breed}")
print(f"the dog named {dog2.name}, weighs {dog2.weight} and is a {dog2.breed}")