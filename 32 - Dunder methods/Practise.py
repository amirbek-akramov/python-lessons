"Practise"

from Practise_module import Person, Location, Student, Subject

math = Subject("Mathematics")
chemistry = Subject("Chemistry")
bilogy = Subject("Biology")
physics = Subject("Pyhsics")


student1_location = Location(34, "Karvon", "Bog'bon", "Uzbekistan")
student1 = Student("Jack", "Jakeson", 1999, "FFBB0001133", 95, student1_location)

student2_location = Location(99, "Yulduz", "Baliqchi", "Uzbekistan")
student2 = Student("Michael", "Jakeson", 2001, "FFBB1112244", 74, student2_location)

student3_location = Location(21, "Yulduz", "Baliqchi", "Uzbekistan")
student3 = Student("Kate", "Michaelson", 2003, "FFBB5553353", 98, student3_location)

student4_location = Location(47, "Yulduz", "Baliqchi", "Uzbekistan")
student4 = Student("Mike", "Williamson", 1982, "FFBB9892322", 14, student4_location)

student5_location = Location(63, "Yulduz", "Baliqchi", "Uzbekistan")
student5 = Student("William", "Mikeson", 1994, "FFBB00100999", 96, student5_location)

student2.set_level(2)
student3.set_level(5)
student5.set_level(3)

math + student1
chemistry.add_students(student3, student5)
bilogy + student4
physics + student2
physics + student3
physics + student1 # "add_students()" or '+'


physics - 95 # id
physics.remove_students(74, 98) # id 

math()
chemistry()
bilogy()
physics()


# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)


