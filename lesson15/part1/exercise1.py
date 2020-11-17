from random import randrange, seed
from datetime import datetime

seed(datetime.now())

my_list = [randrange(0, 100 + 1) for i in range(1500)]

with open("numbers.txt", "w") as f:
    for number in my_list:
        f.write(f"{number}\n")
