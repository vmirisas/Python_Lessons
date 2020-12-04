class Base:
    def __init__(self):
        self.__bpr_attr = 1  # protected member


class Derived(Base):
    def __init__(self):
        super().__init__()



d = Derived()
print(d._Base__bpr_attr)  # error?
