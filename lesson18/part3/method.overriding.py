class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

    def express(self):
        if self.hunger > 5:
            print("Mooooooooooooow")
        else:
            print("Mooww")


class TexasLonghorn(Cow):
    def __init__(self, weight, hunger, horn_length):
        super().__init__(weight, hunger)
        self.horn_length = horn_length

    def express(self):
        if self.hunger > 5:
            print("Mow goes the longhorned cow")
        else:
            print("Silence and piece for our longhorned cow")

molly = Cow(500, 10)
molly.express()

bob = TexasLonghorn(400, 20, 0.50)
bob.express()
