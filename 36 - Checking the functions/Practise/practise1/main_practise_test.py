import unittest
from practise_module import the_biggest

class TestTheBiggestNumber(unittest.TestCase):
    def test_biggest_number(self):
        self.assertEqual(the_biggest(3,7,4), 7)

unittest.main()