"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""

# ValueError

age = input("Write your age: ")

try:
    age = int(age)
    
except ValueError:
    print("Please, write integer. (not float)")

else:
    print(f"Your birth year is {2023 - age}")
    
print("Programm is continue to work")
print("Programm is stopped")