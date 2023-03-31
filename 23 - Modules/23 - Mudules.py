
"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 23-dars: Modules
sana: 11/03/2023
"""

# import auto_info_collecter
# You can use 'as' for reducting the name
# import auto_info_collecter as aic

# auto1 = aic.auto_info("nissan", "skyline", "blue", "auto", 2008, 120_000)
# aic.auto_print(auto1)


"""
If you don't want to write like: aic.auto_print()
Use from ... import ...
_______________________________________________________________________________
"""

# from auto_info_collecter import auto_info, auto_print

# auto1 = auto_info("nissan", "skyline", "blue", "auto", 2008, 120_000)
# auto_print(auto1)

"""
You 'as'.

_______________________________________________________________________________
"""

# from auto_info_collecter import auto_info as ainfo, auto_print as aprint

# auto1 = ainfo("nissan", "skyline", "blue", "auto", 2008, 120_000)
# aprint(auto1)


"""
If you want to import all functions in module
Use *
But do'nt use it if your module is very big

_______________________________________________________________________________
"""

# from auto_info_collecter import *

# auto1 = ainfo("nissan", "skyline", "blue", "auto", 2008, 120_000)
# aprint(auto1)


"""
More default modules in python
Let's look them =>
_______________________________________________________________________________
Example:
math
"""

# import math

# x=400
# print(math.sqrt(x))
# print(math.pow(5,3))
# print(math.pi)
# print(math.log2(8))
# print(math.log10(100))


"""
Other module "random"

_______________________________________________________________________________
"""
"""
Mini game
"""
import random as rm


# randint()
# random integer

# RANDOM_NUMBERS = int(input("Average number for game: "))

# print("Random number is active!")
# number = rm.randint(0, RANDOM_NUMBERS+RANDOM_NUMBERS+50)

# while True:
#     NUMBER2 = rm.randint(0, RANDOM_NUMBERS+RANDOM_NUMBERS+50)
    
#     if NUMBER2 < number:
#         print(f"{NUMBER2} < random number")
#         USER = int(input("Answer: "))
    
#     if NUMBER2 > number:
#         print(f"{NUMBER2} > random number")
#         USER = int(input("Answer: "))
    
    
#     if USER == number:
#         print(f"Answer is correct: {USER}")
#         break




# choise ()

# names = ["jack", "john", "william", "mike", "kite"]

# name = rm.choice(names)
# print(name.title())


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#

# names = ["jack", "john", "william", "mike", "kite"]

# name = rm.choice(names)
# n = rm.choice(name)

# print(name.title())
# print(n)


# x = list(range(0,51,5))
# print(x)
# print(rm.choice(x))


# shuffle ()

# x = list(range(11))
# print(x)
# rm.shuffle(x)
# print(x)