"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 21-dars: Passing a list to a function
sana: 10/03/2023
"""

# def check(names):
#     marks = {}
#     while names:
#         name = names.pop()
#         mark = input(f"What's the mark of {name.title()}: ")
#         marks[name] = int(mark)
#     return marks


# names = [
#     "jack",
#     "john",
#     "william",
#     "i forget name"
# ]
# print(check(names))

"""
Practise 1

_______________________________________________________________________________
"""

# def first_big_letter(names):
#     titled = []
#     while names:
#         name = names.pop()
#         titled.append(name.title())
#     return titled

# names = [
#     "whale",
#     "goat",
#     "cow",
#     "sheep"
# ]

# print(first_big_letter(names))

"""
Practise 2

_______________________________________________________________________________
"""


# def first_big_letter(names):
#     names = names[:]
#     titled = []
#     while names:
#         name = names.pop()
#         titled.append(name.title())
#     return titled

# names = [
#     "whale",
#     "goat",
#     "cow",
#     "sheep"
# ]


# new_names = first_big_letter(names)
# print(new_names)
# print(names)



"""
Practise 3

_______________________________________________________________________________
"""


# def check(names):
#     marks = {}
#     for name in names:
#         mark = input(f"What's the mark of {name.title()}: ")
#         marks[name] = int(mark)
#     return marks


# names = [
#     "jack",
#     "john",
#     "william",
#     "i forget name"
# ]
# print(check(names))
# print(names)

