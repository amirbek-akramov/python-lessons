"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 24-dars: Lambda (unnamed functions)
sana: 12/03/2023
"""

import math

"""
Lambda function don't need name
_______________________________________________________________________________
Lambda creates like this:
    
lambda argument, argument1, argument2: 
    value = argument1 + argument2
    
"""

# lenght = lambda pi, radius: 2*pi*radius
# print(lenght(math.pi, 3))



# number = lambda x,y: x**y
# print(number(5, 2))


"""
Use lambda like this:
"""

# def number(n):
#     return lambda x: x**n

# square_of_number = number(2)
# cube_of_number = number(3)

# print(f"Square of 5 equal to {square_of_number(5)}")
# print(f"Cube of 3 equal to {cube_of_number(3)}")
# print(f"Square of 7 equal to {square_of_number(7)}")
# print(f"Cube of 7 equal to {cube_of_number(7)}")
# print(f"Square of 9 equal to {square_of_number(9)}")
# print(f"Cube of 4 equal to {cube_of_number(4)}")
