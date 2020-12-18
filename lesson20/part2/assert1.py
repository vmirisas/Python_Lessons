def my_sum(sth):
    s = 0
    for item in sth:
        s += item
    return s


def my_sum_new(*numbers):
    s = 0
    for number in numbers:
        s += int(number)
    return s


assert my_sum((1, 2, 3)) == 6
assert my_sum([1, 2, 3]) == 6
assert my_sum({2, 3}) == 5
assert my_sum([2, 5, 6, 4, 7, 4]) == 28
