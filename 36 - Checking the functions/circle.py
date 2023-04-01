import unittest
from circle_module import getPeremetr, getArea

class CircleTest(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(getArea(5), 78.53981633974483)
    
    def test_circle_peremetr(self):
        self.assertAlmostEqual(getPeremetr(5), 31.41592653589793)
    
unittest.main()