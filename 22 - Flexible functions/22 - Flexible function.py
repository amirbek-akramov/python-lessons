"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 22-dars: Flexible function (*args, **kwargs)
sana: 10/03/2023
"""

"""
*args = *arguments

arguments
^^^     ^
arg     s

args
_______________________________________________________________________________

The clone of function "sum()"
"""

# def total(*numbers):
#     total_number = 0
#     for number in numbers:
#         total_number += number
#     return total_number

# print(total(3,5))



"""
** kwargs

keyword arguments
^  ^    ^^^     ^
k  w    arg     s
kwargs

_______________________________________________________________________________
"""


# def auto_info(company, color, **information): # you can give unlimited informations
#     information["company"] = company
#     information["color"] = color
#     return information

# auto1 = auto_info("nissan", "red", year = 1998, name = "RX 7")
# auto2 = auto_info("nissan", "black", name = "skyline", year = 2019, tires = 4, nitro = True)

# # print(auto1)
# # print(auto2)

# ### For more comfort ###

# for key, value in auto1.items():
#     print(f"{key}: {value}")
    
# print("\n") # for spacing between two informations

# for key, value in auto2.items():
#     print(f"{key}: {value}")


"""
Practise 1

_______________________________________________________________________________
"""


# def total(*numbers):
#     total_number = 1
#     for number in numbers:
#         total_number *= number
#     return total_number

# print(total(3,9,4,3))



"""
Practise 2

_______________________________________________________________________________
"""

# def student_info(surname, name, **information):
#     information['name'] = name
#     information['surname'] = surname
    
#     return information

# student1 = student_info("Johnson", "William", age = 14, birth_year = 2008)
# student2 = student_info("Mikeson", "Jack", birth_place = "D.C")
# student3 = student_info("Alexson", "Benny", job = "web developer", hobby = "photoshop")

# students = [student1, student2, student3]
# # print(students)
# print(student1)
# print(student2)
# print(student3)
