import unittest
from ..part2.assert1 import my_sum_new  # import function to be tested


class MySumTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(my_sum_new(1, 2, 3), 6)

    def test_2(self):
        self.assertEqual(my_sum_new(), 0)
