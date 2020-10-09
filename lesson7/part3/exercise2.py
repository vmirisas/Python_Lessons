from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

i = 0
columns = []
while True:
    column = set()
    random_number = randrange(10, 20)
    column.add(random_number)

    while True:
        random_number = randrange(10, 20)
        if random_number not in column:
            column.add(random_number)
            break



    random_number = randrange(20, 40)
    column.add(random_number)

    while True:
        random_number = randrange(20, 40)
        if random_number not in column:
            column.add(random_number)
            break



    # add even number 1-9
    random_number = 2 * randrange(1, 5)
    column.add(random_number)

    # add first number 40-49
    random_number = randrange(41, 49, 2)
    if random_number:
        column.add(random_number)

    if column not in columns:
        columns.append(column)
        i += 1
        if i == 10:
            break

for column in columns:
    print(column)
