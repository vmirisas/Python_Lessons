class A:
    def __init__(self):
        print("Entering A")
        super().__init__()
        print("Exiting A")


class B1(A):
    def __init__(self):
        print("Entering B1")
        super().__init__()
        print("Exiting B1")


class B2(A):
    def __init__(self):
        print("Entering B2")
        super().__init__()
        print("Exiting B2")


class B3(A):
    def __init__(self):
        print("Entering B3")
        super().__init__()
        print("Exiting B3")


class C(B1, B3, B2):
    def __init__(self):
        print("Entering C")
        super().__init__()
        print("Exiting C")


print(C.mro())

C()
