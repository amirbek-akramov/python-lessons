"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 24.1-dars: Lambda (unnamed functions)
sana: 12/03/2023
"""

# from math import sqrt

# numbers = list(range(11))
# roots = list(map(sqrt,numbers))

# print(roots)


# def degree(x):
#     return x*x

# print(list(map(degree,numbers)))

"Use lambda"

# print(list(map(lambda x: x*x, numbers)))




#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#




# a = {
#   "first":"one",
#   "second":"two",
#   "third":"three"
# }

# print(list(map(lambda fl,sl:f"{fl.title()}:{sl.title()}", a.keys(),a.values())))


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#


# a = [5,7,4]
# b = [2,6,8]

# print(list(map(lambda fn,sn: fn**sn, a,b)))