from waiter import Waiter
from barista import Barista
from owner import Owner
from random import randrange, seed
from datetime import datetime


def main():
    seed(datetime.now())

    o = Owner("owner", 100000)
    w1 = Waiter("waiter1", 200000)
    w2 = Waiter("waiter2", 200000)
    b = Barista("barista", 300000)

    waiters = [o, w1, w2]
    baristas = [o, b]

    for i in range(10):
        waiters[randrange(len(waiters))].serve(randrange(1, 3 + 1), baristas[randrange(len(baristas))])

    print("")
    o.report()
    w1.report()
    w2.report()
    b.report()


main()
