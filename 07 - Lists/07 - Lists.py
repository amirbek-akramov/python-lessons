"""
# 07-dars: Lists (Ro'yxatlar)
sana: 29/01/2023
"""

# fruits = [
#     "olma", # 0
#     "nok", # 1
#     "anor", # 2
#     "uzum", # 3
#     "banan", # 4
#     "xurmo", # 5
#     "mandarin", # 6
#     "limon", # 7
#     "apelsin", # 8
#     "lime", #9
# ] # fruits list

# print(fruits[4]) 

# costs = [
#     22_000, # 0
#     13_000, # 1
#     73_500, # 2
#     9_000, # 3
#     45_000, # 4
#     -75_000, # 5
#     49.500 # 6
# ] # costs list

# print(costs)

# mix = [
#     90_000,
#     "olma",
#     23_500,
#     "xurmo",
#     34.690_383,
#     "anjir",
#     "nok"
# ] #mixed list

# meva = []
# # empty list

# print(costs)
# print(fruits)
# print(mix[-1])
# print(meva)

# print("Birinchi meva:", fruits[0])
# print("Ikkinchi meva:", fruits[1])

# _____________________________________________________________________________

"""
    Changing the Element
"""

# mix = [
#     34_444,
#     "Changed",
#     "Changed 1",
#     "Changed 2",
#     "Changed numbers 3",
#     56_333       
# ]

# print(mix)

# fruits[0] = "Sitrus"
# fruits[1] = "Ananas"
# fruits[2] = "Mini mandarin"
# fruits[3] = "Cherry"

# print(fruits)

"""
            .append()
"""

# fruits = [
#     "olma",
#     "anor",
#     "xurmo",
#     "mandarin"
# ]

# fruits.append("banan")

# print(fruits)

# cars = [] #Create empty list

# # Add objects

# cars.append("Nexia 3")
# cars.append("Toyato")
# cars.append("Range Rover")
# cars.append("Bugatti")
# cars.append("Porsche")

# print(cars)

# cars = []

# cars.append(input("Omboringizga qanday avtomobil qo'shgan bo'lardingiz: "))
# cars.append(input("Yana: "))
# cars.append(input(">>>: "))
# cars.append(input(">>>: "))
# cars.append(input(">>>: "))
# cars.append(input(">>>: "))
# cars.append(input(">>>: "))
# cars.append(input(">>>: "))
# cars.append(input(">>>: "))

# print("Musur omboringizga manashu avtomobillarni tashladingiz: ", cars)

"""

If you want to add object in the some place of list 

We recommend you method .insert()

# """

# fruits = [
#     "Olma",
#     "Anor",
#     "Xurmo",
#     "Banan",
#     "Lime"
# ]

# # fruits.insert(4, "Ananas")

# # print(fruits)

# """
#     If you want to sugurish some Element
#     We recommend you .pop()
# """

# fruit = fruits.pop(4)

# print(fruit)

# fruit2 = fruits.pop()

# print(fruit2)

"""
                       Homework
"""

# friends = [
#     "Samandar",
#     "Bunyod",
#     "Aziz"
# ]

# print("Faqat akamni sinfidagi " + friends[1])
# print(friends[0] + " qanay??? Choyni yediramizmi?")
# print("Aslida " + friends[2] + "lar 89ta birzning makrabda :|")

# numbers = [
#     -39, # 0
#     94, # 1
#     13.4, # 2
#     10 # 3
# ]

# numbers[2] = 16.8
# numbers.append(89.3)
# numbers.insert(3, 35)
# numbers[0] = numbers.pop(3)
# QPAYK = numbers[0] + numbers[3]

# print(QPAYK)

# _____________________________________________________________________________

# h_humans = [
#     "Imom Buzoriy",
#     "Abu ALi Ibn Sino",
#     "Ulug'bek",
#     "Mirzo Bobur",
#     "Amir Temur"
# ]

# m_humans = [
#     "Bill Gates", 
#     "Ilon Mask", 
#     "Steve Jobs", 
# ]

# bill_g = m_humans.pop(0)
# amir_temur = h_humans.pop(-1)

# print("In modarn time, I want to be like " + bill_g)
# print("My name like " + amir_temur + " but it means other")

# _____________________________________________________________________________

# friends = []

# friends.append("TailWind Css"),
# friends.append("Bootstrap"),
# friends.append("HTML"),
# friends.append("CSS"),
# friends.append("React")

# print(friends)

# friends.remove("HTML")
# friends.remove("React")

# print(friends)

# friends.insert(0, "Angular")
# friends.insert(3, "Python")
# friends.insert(-1, "JavaScript")

# print(friends)

# not_use = []

# not_use.append(friends.pop(-1))
# not_use.append(friends.pop(-1))
# not_use.append(friends.pop(-1))
# friends.append("Python")

# print("Not used languages of programming:", not_use)
# print("Usefull languages of programming:", friends)
