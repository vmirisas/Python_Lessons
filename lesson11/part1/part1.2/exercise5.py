def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


def is_square(number):
    i = 0
    sq = 0
    while sq < number:
        i += 1
        sq = i * i
    return sq == number



def is_cube(number):
    i = 0
    cub = 0
    while cub < number:
        i += 1
        cub = i * i * i
    return cub == number
print(f"\t\tODD\t\t|\tEVEN\t|\tPRIME\t|\tSQUARE\t|\tCUBE")
for i in range(1,100+1):

    print(f"{i}\t:\t{is_odd(i)}\t,\t{is_even(i)}\t,\t{is_prime(i)}\t,\t{is_square(i)}\t,\t{is_cube(i)}")