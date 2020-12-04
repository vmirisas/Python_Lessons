class Base:
    def __init__(self):
        self._bpr_attr = 1  # protected member


class Derived(Base):
    def __init__(self):
        super().__init__()
        print(self._bpr_attr)  # works fine


d = Derived()
print(d._bpr_attr)  # error?
