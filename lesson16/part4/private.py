class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.__hunger = hunger

    def express(self):
        if self.__hunger > 5:
            print("Moooooooooooooooooooooww")
        else:
            print("Moow")


molly = Cow(100, 5)
print(molly.__hunger)
print(molly.weight)
molly.express()
