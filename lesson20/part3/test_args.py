import unittest

from ..part2.assert1 import my_sum_new, my_sum  # import function to be tested


class MySumTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(my_sum_new(1, 2, 3), 6)

    def test_2(self):
        self.assertEqual(my_sum_new(), 0)

    def test_3(self): # trying multiple things to test
        #the 2 previous tests
        self.assertEqual(my_sum_new(1, 2, 3), 6)
        self.assertEqual(my_sum_new(), 0)
        #========================================
        self.assertEqual(my_sum([4, 4, 4]), 12)
        self.assertEqual(my_sum_new(1 * 2, 5), 7)
