import unittest
from practise_module import sort_the_numbers

class NumberSortedTest(unittest.TestCase):
    def test_sorted_numbers(self):
        even_list_test = [0, 2, 4, 6, 8, 10]
        odd_list_test = [1, 3, 5, 7, 9]
        self.assertEqual(sort_the_numbers(0, 11), even_list_test)
        self.assertEqual(sort_the_numbers(0,11, False), odd_list_test)

unittest.main()