class Base:
    def __init__(self, b_attr):
        self.b_attrib = b_attr

    def __str__(self):
        return "some info about the base class"


class Derived(Base):
    def __init__(self, b_attr, d_attr):
        super().__init__(b_attr)
        self.d_attr = d_attr

    def __str__(self):
        return "Some info about the derived class"

    def giga_info(self):
        return f"{super().__str__()} AND {self.__str__()}"


d = Derived(1, 2)
print(d)
print(d.giga_info())
