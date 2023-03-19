"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 24.2-dars: Lambda (unnamed functions)
sana: 12/03/2023
"""

import random as rm

# numbers = rm.sample(range(100),10)
# print(list(map(lambda x:x%2==0, numbers)))

# filter()


# even_number = list(filter(lambda x:x%2==0, numbers))
# print(even_number)


fruits = ["apple","pineapple","pear","pomegranate","fig","cherry","apricot","peach"]
# search = "a"
# search_a = list(filter(lambda fruit:fruit.startswith(search), fruits))
# search_a = list(filter(lambda fruit:fruit.startswith(search) and fruit.endswith('t'), fruits))
# print(search_a)

search = list(filter(lambda fruit:len(fruit)<=5, fruits))
print(search)