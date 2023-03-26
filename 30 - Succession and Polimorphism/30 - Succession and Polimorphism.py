"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#30 - lesson: Succession and Polimorphism
Date: 21/03/2023
"""

class Person:
    """Create a person"""
    def __init__(self, name, surname, birth_year, passport):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.passport = passport
    
    def get_age(self, year = 2023):
        return year - self.birth_year
            
    def get_info(self):
        """Returns information about person"""
        return f"Person's information: \n Name: {self.name.title()} \n Surname: {self.surname.title()} \n Age: {self.year - self.birth_year}"
    
    def get_birth_year(self):
        """Birth year of person"""
        return self.birth_year
    
    def get_passport(self):
        password = input("Enter the password: ")
        return self.passport if password == "see_passport1234" else "Invalid password"
    
# person1 = Person("Mike", "Williamson", 1973, "FFBB1102255")
# print(person1.get_info())

"""_________________________________________________________________________"""

class Location:
    """Location"""
    def __init__(self, house, street, town, country):
        self.house = house
        self.street = street
        self.town = town
        self.country = country
        
    def get_location(self):
        """Returns the location"""
        return f"Location: \n  House: {self.house} \n  Street: {self.street} \n  Town: {self.town} \n  Country: {self.country}"


"""________________________________Succession_______________________________"""


class Student(Person):
    def __init__(self, name, surname, birth_year, passport, ID, location):
        super().__init__(name, surname, birth_year, passport)
        self.ID = ID
        self.level = 1
        self.location = location
    
    def set_level(self, level):
        self.level = level
        return "Level successfully added"
    
    def get_level(self):
        """Returns level of student"""
        return self.level    
        
    def get_id(self):
        """Returns id of student"""
        return self.ID

    def get_info(self):
        """Returns information about student"""
        return f"Student's information: \n Name: {self.name.title()} \n Surname: {self.surname.title()} \n Age: {self.get_age()} \n Id: {self.ID} \n Level: {self.level} \n\n {self.location.get_location()}"
    

student1_location = Location(34, "Karvon", "Bog'bon", "Bukhara")
student1 = Student("Jack", "Jakeson", 1999, "FFBB0001133", 95, student1_location)
print(student1.get_info())



        