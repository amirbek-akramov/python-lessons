"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#28 - lesson: Classes
Date: 17/03/2023
"""

"""
Class is mould for objects 
"""

# Classes need to create like this: 

# class Student:
#     def __init__(self,name,surname,birth_year,email):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year
#         self.email = email
        
#     def get_name(self):
#         return self.name
        
#     def get_surname(self):
#         return self.surname
        
#     def get_birth_year(self):
#         return self.birth_year
        
#     def get_email(self):
#         return self.email
        
#     def get_age(self, year):
#         return year - self.birth_year
        
#     def introduce(self):
#         # Don't write "print", becouse you write less programmes with console
#         # print(f"Student info: \n Code: {student1}. \n Name: {name} \n Surname: {surname} \n E-mail: {email}")
#         "Write return for more usefull code"
#         return f"Student info: \n Code: {student1}. \n Name: {self.name} \n Surname: {self.surname} \n E-mail: {self.email}"


# student1 = Student("Amirbek", "Akramov", 2010,"amirekcoder@gmail.com")



"""
Practise

_______________________________________________________________________________
"""

# class User:
#     def __init__(self, name, surname, birth_year, email = None, password = None):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year
#         self.email = email
#         self.password = password
        
#     def get_info(self, year):
#         self.year = year
#         return f"User info: \n Name: {self.name} \n Surname: {self.surname} \n Age: {year - self.birth_year}."
    
#     def secret_info(self):
#         return f"E-mail: {self.email} \nPassword: *********"
    
#     def get_email(self):
#         return self.email
    
#     def get_password(self):
#         return self.password
        
# name = input("Name: ")
# surname = input("Surname: ")
# birth_year = int(input("Birth year: "))
# email = input("Email: ")
# password = input("Password: ")
    
# user1 = User(name, surname, birth_year, email, password)
