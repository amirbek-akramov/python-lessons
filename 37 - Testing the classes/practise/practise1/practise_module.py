class Person:
    __person_amount = 0
    """Create a person"""
    def __init__(self, name, surname, birth_year, passport, __health):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.passport = passport
        self.__health = __health
        Person.__person_amount += 1
    
    @classmethod
    def get_person_amount(cls):
        return cls.__person_amount

    def get_about_health(self):
        return self.__health

    def set_health(self, __health):
        self.__health = __health

    def get_age(self, year = 2023):
        return year - self.birth_year
            
    def get_info(self):
        """Returns information about person"""
        return f"Person's information: \n Name: {self.name.title()} \n Surname: {self.surname.title()} \n Age: {self.get_age()}"
    
    def get_birth_year(self):
        """Birth year of person"""
        return self.birth_year
    
    def get_passport(self):
        password = input("Enter the password: ")
        return self.passport if password == "see_passport1234" else "Invalid password"

"""________________________________Location_______________________________"""

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


"""________________________________Student_______________________________"""


class Student(Person):
    __student_amount = 0
    def __init__(self, name, surname, birth_year, passport, __health, __hobby, ID, location):
        super().__init__(name, surname, birth_year, passport, __health)
        self.ID = ID
        self.level = 1
        self.location = location
        self.__hobby = __hobby
        Student.__student_amount += 1
        
    @classmethod
    def get_hobby(cls):
        """Student's hobby"""
        return cls.__hobby
    
    def set_hobby(self,hobby):
        """Changing the hobby of student"""
        self.__hobby = hobby
    
    def set_level(self, level):
        self.level = level
        return "Level successfully added"
    
    def get_level(self):
        """Returns level of student"""
        return self.level    
        
    def get_id(self):
        """Returns id of student"""
        return self.ID

    def get_location(self):
        return self.location

    def get_info(self):
        """Returns information about student"""
        return f"Student's information: \n Name: {self.name.title()} \n Surname: {self.surname.title()} \n Age: {self.get_age()} \n Id: {self.ID} \n Level: {self.level} \n Hobby: {self.__hobby} \n\n {self.location.get_location()}"


student1_location = Location(34, "Karvon", "Bog'bon", "Uzbekistan")
student1 = Student("Jack", "Jakeson", 1999, "FFBB0001133", False, "Writing", 1.0, student1_location)

student2_location = Location("2468", "Elm St", "Villagetown", "USA")
student2 = Student("John", "Doe", 2000, "123456789", True, "Reading", 1.1, student2_location)

student3_location = Location("1357", "Maple Ave", "Citytown", "Canada")
student3 = Student("Jane", "Smith", 1999, "987654321", False, "Painting", 1.2, student3_location)

student4_location = Location("3691", "Pine St", "Beachtown", "Australia")
student4 = Student("Tom", "Jones", 2001, "555555555", True, "Playing sports", 1.3, student4_location)


if __name__ == "__main__":
    print(student1.get_info(), end="\n\n\n\n")
    print(student2.get_info(), end="\n\n\n\n")
    print(student3.get_info(), end="\n\n\n\n")
    print(student4.get_info())

    print(student1_location.get_location())
    print(student2_location.get_location())
    print(student3_location.get_location())
    print(student4_location.get_location())