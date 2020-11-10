def factory(a, b, c):
    def polynomial(x):
        print(f"for x = {x}")
        return a * x ** 2 + b * x + c

    print(f"{a}*x^2 + {b}*x + {c} => ")
    return polynomial


pol = factory(1, 1, 1)
print(f"{pol(4)}")
