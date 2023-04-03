"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#38 - lesson: Standart modules of python
Date: 03/04/2023 // 8:10
"""

import math

# math

PI = math.pi
print(f"Value of pi: {PI}")

E = math.e
print(f"Value of e: {E}")

# Trigonometry

math.sin(math.pi/2)
math.cos(0)
math.tan(PI)

# Radians and degrees

math.degrees(math.pi/2)
math.radians(90)

# LOGARIFMS

# natural logarifm
math.log(5)
# 10 oriented logarifm
math.log10(100)

# Rounding the numbers

x = 4.6
print(math.ceil(x))
print(math.floor(x))
"""You can use 'round' for rounding the numbers more easily"""

# Root and level

x = 81

# Square root
math.sqrt(x)

# Raising the number to a power
math.pow(x,3) # x's cube
math.pow(x,5) # x's 5th degree
math.pow(x,1/3) # cobe root from x
