import unittest
from practise_module import Student, Location

# one test for two classes

class StudentLocationTest(unittest.TestCase):
    def setUp(self):
        self.student1_location = Location(34, "Karvon", "Bog'bon", "Uzbekistan")
        self.student1 = Student("Jack", "Jakeson", 1999, "FFBB0001133", False, "Writing", 1.0, self.student1_location)

        self.student2_location = Location("2468", "Elm St", "Villagetown", "USA")
        self.student2 = Student("John", "Doe", 2000, "123456789", True, "Reading", 1.1, self.student2_location)

        self.student3_location = Location("1357", "Maple Ave", "Citytown", "Canada")
        self.student3 = Student("Jane", "Smith", 1999, "987654321", False, "Painting", 1.2, self.student3_location)

        self.student4_location = Location("3691", "Pine St", "Beachtown", "Australia")
        self.student4 = Student("Tom", "Jones", 2001, "555555555", True, "Playing sports", 1.3, self.student4_location)

    def test_location(self):
        self.assertEqual(self.student1_location, self.student1.location)
        self.assertEqual(self.student2_location, self.student2.location)
        self.assertEqual(self.student3_location, self.student3.location)
        self.assertEqual(self.student4_location, self.student4.location)

    def test_health(self):
        self.assertFalse(self.student1.get_about_health())
        self.assertFalse(self.student3.get_about_health())

        self.assertTrue(self.student2.get_about_health())
        self.assertTrue(self.student4.get_about_health())

    def test_class(self):
        self.assertTrue(isinstance(self.student1_location, Location))
        self.assertTrue(isinstance(self.student2_location, Location))
        self.assertTrue(isinstance(self.student3_location, Location))
        self.assertTrue(isinstance(self.student4_location, Location))

    def test_student_location(self):
        self.assertTrue(isinstance(self.student1.location, Location))
        self.assertTrue(isinstance(self.student2.location, Location))
        self.assertTrue(isinstance(self.student3.location, Location))
        self.assertTrue(isinstance(self.student4.location, Location))

    def test_student(self):
        self.assertTrue(isinstance(self.student1, Student))
        self.assertTrue(isinstance(self.student2, Student))
        self.assertTrue(isinstance(self.student3, Student))
        self.assertTrue(isinstance(self.student4, Student))

    def test_get_info(self):
        self.assertEqual(self.student1.get_info(), "Student's information: \n Name: Jack \n Surname: Jakeson \n Age: 24 \n Id: 1.0 \n Level: 1 \n Hobby: Writing \n\n Location: \n  House: 34 \n  Street: Karvon \n  Town: Bog'bon \n  Country: Uzbekistan")
        self.assertEqual(self.student2.get_info(), "Student's information: \n Name: John \n Surname: Doe \n Age: 23 \n Id: 1.1 \n Level: 1 \n Hobby: Reading \n\n Location: \n  House: 2468 \n  Street: Elm St \n  Town: Villagetown \n  Country: USA")
        self.assertEqual(self.student3.get_info(), "Student's information: \n Name: Jane \n Surname: Smith \n Age: 24 \n Id: 1.2 \n Level: 1 \n Hobby: Painting \n\n Location: \n  House: 1357 \n  Street: Maple Ave \n  Town: Citytown \n  Country: Canada")
        self.assertEqual(self.student4.get_info(), "Student's information: \n Name: Tom \n Surname: Jones \n Age: 22 \n Id: 1.3 \n Level: 1 \n Hobby: Playing sports \n\n Location: \n  House: 3691 \n  Street: Pine St \n  Town: Beachtown \n  Country: Australia")

    def test_get_location(self):
        self.assertEqual(self.student1_location.get_location(), "Location: \n  House: 34 \n  Street: Karvon \n  Town: Bog'bon \n  Country: Uzbekistan")
        self.assertEqual(self.student2_location.get_location(), "Location: \n  House: 2468 \n  Street: Elm St \n  Town: Villagetown \n  Country: USA")
        self.assertEqual(self.student3_location.get_location(), "Location: \n  House: 1357 \n  Street: Maple Ave \n  Town: Citytown \n  Country: Canada")
        self.assertEqual(self.student4_location.get_location(), "Location: \n  House: 3691 \n  Street: Pine St \n  Town: Beachtown \n  Country: Australia")

if __name__ == "__main__":
    unittest.main()        
