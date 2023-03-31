"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""

# Solve the problems if you can

while True:
    age = input("Write your age: ")

    if age:
        if age.isdigit():
            age = int(age)
        
        else:
            print("Please, write integer. (not float)")
    else:
        print("Programm was stopped")
        break
        
    print(f"Your birth year is {2023 - age}")
    