"Practise"

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
    __student_amount = 0
    def __init__(self, name, surname, birth_year, passport, __health, ID, location):
        super().__init__(name, surname, birth_year, passport, __health)
        self.ID = ID
        self.level = 1
        self.location = location
        Student.__student_amount += 1
    
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