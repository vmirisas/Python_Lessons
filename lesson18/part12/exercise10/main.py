from circle import CircleResizable


def main():
    c = CircleResizable(1)
    print(c.area(), c.perimeter())
    c.resize(2)
    print(c.area(), c.perimeter())


main()
