
class Person:
    """Create a person"""
    def __init__(self, name, surname, birth_year, passport):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.passport = passport
    
    def get_age(self, year = 2023):
        return year - self.birth_year
            
    def __repr__(self):
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
        
    def __repr__(self):
        """Returns the location"""
        return f"Location: \n  House: {self.house} \n  Street: {self.street} \n  Town: {self.town} \n  Country: {self.country}"



"""________________________________Succession_______________________________"""


class Student(Person):
    def __init__(self, name, surname, birth_year, passport, ID, location, __level=1):
        super().__init__(name, surname, birth_year, passport)
        self.ID = ID
        self.__level = __level
        self.location = location
    
    def set_level(self, level):
        self.__level = level
        return "Level successfully added"
    
    def get_level(self):
        """Returns level of student"""
        return self.__level    
        
    def get_id(self):
        """Returns id of student"""
        return self.ID

    def __repr__(self):
        """Returns information about student"""
        return f"\nStudent's information: \n Name: {self.name.title()} \n Surname: {self.surname.title()} \n Age: {self.get_age()} \n Id: {self.ID} \n Level: {self.__level} \n\n {self.location}\n\n"
    

    def __lt__(self,y):
        return self.__level < y

    def __le__(self,y):
        return self.__level <= y

    def __gt__(self,y):
        return self.__level > y

    def __ge__(self,y):
        return self.__level >= y

    def __eq__(self,y):
        return self.__level == y
    
    def __ne__(self, y):
        return self.__level != y


"""_________________________________________________________________________"""


class Subject:
    __students_amount = 0
    def __init__(self, name):
        self.name = name
        self.subject_students = []
        Subject.__students_amount += 1


    @classmethod

    def __repr__(cls):
        return f"We have {cls.__students_amount} students general"

    def __add__(self, student):
        if isinstance(student, Student):
            self.subject_students.append(student)
        else:
            print("You can add student(s) only from 'Student' class")

    def add_students(self, *students):
        for student in students:
            if isinstance(student, Student):
                self.subject_students.append(student)
            else:
                print("You can add student(s) only from 'Student' class")

    def __sub__(self, student_id):
        for subject_student in self.subject_students:
            if subject_student.ID == student_id:
                self.subject_students.remove(subject_student)
            else:
                print(f"Not founded: Student with {student_id} id.")

    def remove_students(self, *students_id):
        for student_id in students_id:
            for subject_student in self.subject_students:
                if subject_student.ID == student_id:
                    self.subject_students.remove(subject_student)
                else:
                    print(f"Not founded: Student with {student_id} id.")

    def __call__(self):
        print(f"\n{self.name}: \n ", [student for student in self.subject_students])

    @classmethod

    def __lt__(self,y):
        return self.__subject_amount < y

    def __le__(self,y):
        return self.__subject_amount <= y

    def __gt__(self,y):
        return self.__subject_amount > y

    def __ge__(self,y):
        return self.__subject_amount >= y

    def __eq__(self,y):
        return self.__subject_amount == y

    def __ne__(self,y):
        return self.__subject_amount != y

    #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#

    def __getitem__(self,index):
        return self.subject_students[index]

    def __setitem__(self,index,value):
        self.subject_students[index] = value

    def __len__(self):
        return len(self.subject_students)