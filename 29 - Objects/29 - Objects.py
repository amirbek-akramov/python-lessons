"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#29 - lesson: Objects
Date: 18/03/2023
"""

"Always active (Function that print the classes' methods)"

def see_methods(value):
    # Class or object. Illustrate the all methods of classes or objects
    return [method for method in dir(value) if not method.startswith("__")]

def see_default_methods(value):
    # Class or object. Illustrate the all default methods of classes or objects
    return [method for method in dir(value) if method.startswith("__")]


"Classic classes"

# class Student:
#     def __init__(self, name, surname, birth_year):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year
        
#     def get_info(self, year):
#         return f"Student's info: \n Name: {self.name} \n Surname: {self.surname} \n Age: {year - self.birth_year}"
    
    
"Classes with default value"

# class Student:
#     def __init__(self, name, surname, birth_year):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year
#         self.course = 1
        
#     def get_info(self, year):
#         return f"Student's info: \n Name: {self.name} \n Surname: {self.surname} \n Age: {year - self.birth_year}"


"I recommend you using method in order to  writing like this 'name.argument' "

# class Student:
#     def __init__(self, name, surname, birth_year):
#         self.course = 1
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year

#     def get_name(self):
#         return self.name
    
#     def get_surname(self):
#         return self.surname
        
#     def get_birth_year(self):
#         return self.birth_year
    
#     def get_course(self):
#         return self.course

#     def set_course(self, course):
#         self.course = course
        
#     def update_course(self):
#         self.course += 1
        
#     def get_age(self, year=2023):
#         return year - self.birth_year
        
            
#     def get_info(self):
#         return f"Student's info: \n Name: {self.name} \n Surname: {self.surname} \n Age: {self.get_age()} \n Course: {self.course}"

# student1 = Student("Mike", "Willson", 1989)

# student1.set_course(4)
# print("Before updating course method:", end = " ")
# print(student1.get_course())


# student1.update_course()
# print("After updating course method: ", end = "")
# print(student1.get_course())


"""
_______________________________________________________________________________
"""

# class Student:
#     def __init__(self, name, surname, birth_year):
#         self.course = 1
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year

#     def get_name(self):
#         return self.name
    
#     def get_surname(self):
#         return self.surname
        
#     def get_birth_year(self):
#         return self.birth_year
    
#     def get_course(self):
#         return self.course

#     def set_course(self, course):
#         self.course = course
        
#     def update_course(self):
#         self.course += 1
        
#     def get_age(self, year=2023):
#         return year - self.birth_year
    
#     def get_fullname(self):
#         return f"{self.name} {self.surname}"
        
            
#     def get_info(self):
#         return f"Student's info: \n Name: {self.name} \n Surname: {self.surname} \n Age: {self.get_age()} \n Course: {self.course}"


# class Subject:
#     def __init__(self,subject):
#         self.subject = subject
#         self.students_amount = 0
#         self.students = []
        
#     def add_student(self, student):
#         self.students.append(student)
#         self.students_amount += 1
        
#     def remove_student(self, student):
#         self.students.remove(student)
#         self.students_amount -= 1
        
#     def get_subject_name(self):
#         return self.subject
    
#     def get_students_middle_age(self):
#         # If all students in one subject
#         middle_age = 0
#         for student in self.students:
#             middle_age += student.get_age()
#         return middle_age / len(self.students)
    
#     def get_students_names(self):
#         return [student.get_name() for student in self.students]
    
#     def get_students_surnames(self):
#         return [student.get_surname() for student in self.students]
    
#     def get_students_full_names(self):
#         return [student.get_fullname() for student in self.students]

#     def get_students_info(self):
#         return [student.get_info() for student in self.students]
    

# chemistry = Subject("Chemistry")
# math = Subject("Mathematics")

# student1 = Student("Ali", "Valiyev", 2020)
# student2 = Student("Shohjahon", "Alimov", 1973)
# student3 = Student("Hasan", "Boriyev", 2020)
# student4 = Student("Husan", "Bariyev", 1999)
# student5 = Student("Akrom", "Hasanov", 1982)
# student6 = Student("Vali", "Husanov", 2020)

# math.add_student(student3)
# math.add_student(student6)
# math.add_student(student1)

# chemistry.add_student(student2)
# chemistry.add_student(student4)
# chemistry.add_student(student5)


# print(math.students_amount)
# print(math.get_students_full_names())
# print(chemistry.get_students_full_names())


"""
Practise 1

_______________________________________________________________________________
"""

class Auto:
    def __init__(self,model,color,cost,auto_type="mannual"):
        self.model = model
        self.color = color
        self.cost = cost
        self.auto_type = auto_type
        self.km = 0
        self.extra_tire = 1
        self.dizel_motor = False
        
    def get_info(self):
        "Information about auto"
        return f"Car info: \n Model: {self.model} \n Color: {self.color} \n Type: {self.auto_type}"

    def get_model(self):
        "Model of auto"
        return self.model
    
    def get_color(self):
        "Color of auto"
        return self.color
    
    def get_cost(self):
        "Cost of auto"
        return f"{self.cost}$"
    
    def get_type(self):
        "Type of auto"
        return self.auto_type
    
    def get_drived_km(self):
        return self.km
    
    def add_km(self):
        self.km += 1
    
    def set_km(self, km):
        self.km = km
    
    def get_extra_tire(self):
        return self.extra_tire
    
    def add_extra_tire(self):
        self.extra_tire += 1
        
    def set_extra_tire(self, extra_tire):
        self.extra_tire = extra_tire
            
    def get_motor_dizel(self):
        return self.dizel_motor
    
    def change_motor_dizel(self):
        if not self.dizel_motor:
            self.dizel_motor = True 
        else:
            self.dizel_motor = False
        
class AutoStore:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.auto_amount = 0
        self.autos = []
        
    def add_car(self,car):
        self.auto_amount += 1
        self.autos.append(car)
        
    def get_info(self):
        cars = []
        [cars.append(auto.get_model()) for auto in self.autos]
        return f"\nAuto store: {self.name.title()} \n Cars: {self.auto_amount} \n Models: {cars}"
    
    def get_car_models(self):
        return [auto.get_model() for auto in self.autos]

car1 = Auto("Ferrari", "red", 200_000,"mannual")
car2 = Auto("M26 ferio", "gray", 240_000,"auto")
car3 = Auto("Skyline", "black", 270_000,"auto")
car4 = Auto("R32 ferio", "blue", 300_000,"mannual")
car5 = Auto("Mustang GT", "red", -200_000,"auto")
car6 = Auto("Hammer", "red", 500_000,"mannual")
car7 = Auto("Widow", "black", 180_000,"auto")
car8 = Auto("Aventador", "red", 500_000,"mannual")
car9 = Auto("Cheron Sport", "Blue", 800_000,"auto")
car10 = Auto("Cheron", "Blue", 800_000,"auto")
car11 = Auto("Veron", "Blue", 800_000,"auto")

ferrari = AutoStore("Ferrari", "Italy")
ford = AutoStore("Ford", "America")
lambarghini = AutoStore("Lambarghini", "Italy")
bugatti = AutoStore("BugaTTi", "somewhere")

ferrari.add_car(car1)
ferrari.add_car(car2)
ferrari.add_car(car3)
ferrari.add_car(car4)
ford.add_car(car5)
ford.add_car(car6)
ford.add_car(car7)
lambarghini.add_car(car8)
bugatti.add_car(car9)
bugatti.add_car(car10)
bugatti.add_car(car11)

print(ferrari.get_info())
print(ford.get_info())
print(lambarghini.get_info())
print(bugatti.get_info())
