from Practise_Module import Person, Location, Student

    
person1 = Person("Jack", "Michaelson", 1985, "FFBB3322213", "nice")

student1_location = Location(99, "Karvon", "Umid", "Uzbekistan")
student1 = Student("Mike", "Jackson", 1982, "FFBB9994342", "normal", "Playing tennis", 34, student1_location)

tab_enter = "\n\n\n\n"
print(person1.get_info(), end = tab_enter)
print(student1_location.get_location(), end = tab_enter)
print(student1.get_info(), end = tab_enter)