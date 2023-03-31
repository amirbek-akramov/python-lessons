"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 29/03/2023
"""

age = input("Write your age: ")

try:
    age = int(age)
    print(f"Your birth year is {2023 - age}")

except:
    print("Please, write integer. (not float)")
