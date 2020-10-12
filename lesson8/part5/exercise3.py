from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

dice = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

N = 10

for i in range(N):
    random_number = randrange(1, 6 + 1)
    dice[random_number] += 1
print(dice)

for key, value in dice.items():
    print(str(key) + " : " + str(value / N))
