import unittest
from practise_module import have_fibinacci

class NumberInFibonacciTest(unittest.TestCase):
    def test_number_in_fibonacci(self):
        self.assertEqual(have_fibinacci(8, 10), True)

unittest.main()