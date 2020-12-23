import unittest

from barista import Barista
from waiter import Waiter


class WaiterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.waiter1 = Waiter("Harry Potter", 150)
        self.waiter1.customers_served = 42

        self.barista1 = Barista("Hermione Granger", 160)

    def test_init(self):
        w = Waiter("Ron Weasley", 149)
        self.assertEqual(w.full_name, "Ron Weasley")
        self.assertEqual(w.salary, 149)
        self.assertEqual(w.customers_served, 0)

        self.assertEqual(self.waiter1.full_name, "Harry Potter")
        self.assertEqual(self.waiter1.salary, 150)
        self.assertEqual(self.waiter1.customers_served, 42)

    def test_serve(self):
        # for Ron Weasley
        w = Waiter("Ron Weasley", 149)
        w.serve(54, self.barista1)
        self.assertEqual(w.customers_served, 54)

        # for Harry Potter (has already served 42 and serves +31)
        self.waiter1.serve(31, self.barista1)
        self.assertEqual(self.waiter1.customers_served, 73)

        # for Hermione Granger [54 (from Ron) + 31 (from Harry, the 42 from before don't count as they aren't prepared by barista1)
        self.assertEqual(self.barista1.customers_served, 85)
        print(f"the Barista {self.barista1.full_name} served {self.barista1.customers_served} customers at the end of the test day")
