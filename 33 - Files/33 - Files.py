"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#33 - lesson: Files
Date: 27/03/2023
"""

# for opening the file, use "open()"



# txt_file = open('pi.txt')
# PI = txt_file.read()
# print(PI)
# txt_file.close()


"""
Use other way for more safity

_______________________________________________________________________________
For exapmle this:
"""

# txt_file_name = "txt_file/pi.txt"

# with open(txt_file_name) as txt_file:
#     PI = txt_file.read()
    
# print(PI)

# print("\n\n")

# PI = PI.rstrip()
# PI = PI.replace("\n", "")
# PI = float(PI)
# print(PI)


"""
Open file that is in other file

_______________________________________________________________________________
"""

# txt_file_name = "data/students.txt"

# with open(txt_file_name) as file:
#     for line in file:
#         print(line)

# with open(txt_file_name) as file:
#     students = file.readlines()

# print(students)

# students = [student.rstrip() for student in students]

# print(students)


"""
Writing to file

_______________________________________________________________________________
"""

# txt_file_name = "new_file/new_txt_file.py"
# students = {}

# name = "'Nicholas Anderson'"
# age = 23
# age += 1

# with open(txt_file_name, 'w') as file: # 'w' as write
#     file.write("\nname = " + name + "\n")
#     file.write("age = " + str(age) + "\n")


"""
Use module "pickle"

_______________________________________________________________________________
"""

# import pickle

# txt_file = "info/info"

# # Dictionary 1
# students_dict_1 = {
#     "Emma": "Charlotte",
#     "Liam": "Noah",
#     "Avery": "Harper",
#     "Ethan": "Lucas",
#     "Mia": "Isabella"
# }

# # Dictionary 2
# students_dict_2 = {
#     "Charlotte": "Emma",
#     "Noah": "Liam",
#     "Harper": "Avery",
#     "Lucas": "Ethan",
#     "Isabella": "Mia"
# }

# # Writing

# with open(txt_file, "wb") as file:
#     pickle.dump(students_dict_1, file)
#     pickle.dump(students_dict_2, file)


# # Reading

# with open(txt_file, "rb") as file:
#     students_dict_1 = pickle.load(file)
#     students_dict_2 = pickle.load(file)

# print(students_dict_1)
# print(students_dict_2)