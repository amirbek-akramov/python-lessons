import unittest
from practise_module import names_title

class NamesTitleTest(unittest.TestCase):
    def test_name_titled(self):
        names = ['alice', 'bob', 'charlie', 'david', 'emma', 'frank', 'grace', 'hannah', 'isaac', 'julia']
        titled_names = [name.title() for name in names]
        self.assertEqual(names_title(), titled_names)

unittest.main()