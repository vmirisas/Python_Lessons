from waiter import Waiter
from barista import Barista


class Owner(Waiter, Barista):
    def __init__(self, full_name, salary):
        super().__init__(full_name, salary)
