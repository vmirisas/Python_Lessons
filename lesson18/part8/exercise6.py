class King:
    def __init__(self, kingdom):
        self.kingdom = kingdom

    def rule(self):
        print("Now i rule")


class Philosopher:
    def __init__(self, school):
        self.school = school

    def think(self):
        print("Now i think")


class PhilosopherKing(King, Philosopher):
    def __init__(self, kingdom, school):
        King.__init__(self, kingdom)
        Philosopher.__init__(self, school)

    def routine(self):
        self.think()
        self.rule()
        self.think()


marcus_aurelius = PhilosopherKing("Roman Empire", "Stoic")
marcus_aurelius.routine()
