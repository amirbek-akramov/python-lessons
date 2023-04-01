import unittest as utest # I recomend you use modules wiht full name without "as name". Write full name of module
from main_module import get_full_name


class FunctionTest(utest.TestCase):
    def test(self):
        name = get_full_name("jake", "michaelson")
        self.assertEqual(name, "Jake Michaelson")

    def test_father(self):
        name_father = get_full_name("jake", "michaelson", "jack")
        self.assertEqual(name_father, "Jake Jack Michaelson")
        
utest.main()