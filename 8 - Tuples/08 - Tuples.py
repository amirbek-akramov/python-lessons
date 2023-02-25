"""
# 08-dars: Tuples (O'zgarmas ro'yxatlar)
sana: 31/01/2023
"""

# Sorting

# random_names = [
#     'queen',
#     'wolga',
#     'experiment',
#     'ruby',
#     'tailwind',
#     'yes',
#     'ugly',
#     'imitate',
#     'openAI',
#     'python',
#     'audi',
#     'script',
#     'date',
#     'facebook',
#     'golang',
#     'html',
#     'javascript',
#     'knowledge',
#     'lost',
#     'zipe',
#     'xml',
#     'css',
#     'vue',
#     'bootstrap',
#     'notion',
#     'machinics'
# ]

# names = []

# names.append(input("Ism yoki nom yozing va ularni sortirovka qilamiz: "))
# names.append(input("Ism yoki nom yozing: "))
# names.append(input("Ism yoki nom yozing: "))
# names.append(input("Ism yoki nom yozing: "))
# names.append(input("Ism yoki nom yozing: "))
# names.append(input("Ism yoki nom yozing: "))

# random_names.sort()
# print(sorted(random_names))
# print(random_names)

# _____________________________________________________________________________

"""
            With numbers
# """

# numbers = [
#     -4,
#     -2,
#     1,
#     5,
#     7,
#     8,
#     39,
#     87,
#     25,
#     99,
#     2
# ]


# numbers = []

# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))
# numbers.append(int(input("Son kiriting: ")))

# numbers.sort(reverse=True)

# print(sorted(numbers, reverse=True))

# _____________________________________________________________________________

"""
                Reverse method
"""

# languages = [
#     "JavaScript",
#     "Python",
#     "PHP",
#     "Ruby",
#     "Swift",
#     "Java"
# ]

# languages.reverse()
# print(reversed(languages))

"""
            Lenght of the ...
"""

# languages = input("So'z kiriting: ")

# if len(languages) >= 10:
#     print(f"So'zingiz {len(languages)}ta harfdan iborat")

# else:
#     print(f"So'zingiz {len(languages)}ta harfdan iborat")

# print("Lenght of the list:", len(languages))



"""
            Range method
"""

# newList = list(range(0,10))
# print(newList)


"""
            Range method 2
"""

# newList = list(range(0,101,10))
# print(newList)

"""
            Min |_'-'_| Max
"""
# firstNumber = int(input("Necha so'mdan boshlansin: "))
# secondNumber = int(input("Necha so'mgacha: "))



# newList = list(range(firstNumber, secondNumber + 1_000, 1_000))
# print("Tovarlarimiz narhi:", newList)
# print("Eng qimmat narhi:", max(newList))
# print("Eng arzon narhi:", min(newList))


# text = [
#     "Every",
#     "Day",
#     "Second"
# ]

# print(max(text))

"""
            Sum
"""

# ranGe = list(range(0,101))
# print(ranGe)
# print(sum(ranGe))

"""
            Cutting the List
"""

# langs = [
#     "JavaScript", # 0
#     "Java", # 1
#     "Python", # 2
#     "Kotlin", # 3 <=<=
#     "C", # 4
#     "C++", # 5 <=<=
#     "C#" # 6
# ]

# print(langs[3:6])
# print(langs[:3])  #<=-|
# print(langs[0:3])  #<=|

# print(langs[2:]) # <==--|
# print(langs[2:-1]) # <=-|


"""
            Duplicate the list
"""

# cars = [
#     "BMW",
#     "Tesla",
#     "Nissan",
#     "Toyato",
#     "BugaTTi",
#     "Ferrari",
#     "Lambargini",
#     "Ford Mustang GT"
# ]


# myCars = cars = False
# myCars = cars[:] = True

# myCars.remove("Tesla")
# myCars[0] = "Hyundai"

# print(myCars)
# print(cars)

"""
            Tuples
"""


# cars = (
#     "BMW",
#     "Tesla",
#     "Nissan",
#     "Toyato",
#     "BugaTTi",
#     "Ferrari",
#     "Lambargini",
#     "Ford Mustang GT"
# )

# print(type(cars))
# cars[1] = "Daewoo buuuu"
# cars.append("Ravon")
# cars.remove("BMW")
# lambo = cars.pop("Lambargini")
# cars.insert("Chevrolet", 4)

"""
    When it's very important
"""

# cars = list(cars)
# print(type(cars))  # list
# print(cars)

# cars.append("Labo")

# cars = tuple(cars) # do this after you finish your work with list

# print(type(cars))  # tuple
# print(cars)
