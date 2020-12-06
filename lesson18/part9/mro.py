class A:
    pass


class B1(A):
    pass


class B2(A):
    pass


class C(B1, B2):
    pass


print(C.mro())
