"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""
# Many errors

number = input("Number: ")

try:
    number = int(number)
    x=20
    math = x/number

except ValueError:
    print("Write only integer")

except ZeroDivisionError:
    print("Write number that bigger than zero")

else:
    print(f"{x}/{number} = {math}")

# If you can solve the problem use if else or something else