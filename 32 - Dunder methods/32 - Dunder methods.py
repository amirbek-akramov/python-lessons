"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#32 - lesson: Dunder methods
Date: 26/03/2023
"""
from Dunder_methods_module import Auto, AutoStore



car1 = Auto("Lambarghini", "Aventador", "black", 2020, 240_000, 15_000)
car2 = Auto("Kia", "K5", "white", 2013, 110_000)
car3 = Auto("BMW", "R7", "dark_black", 2016, 210_000, 100, False)
car4 = Auto("BugaTTi", "Cheron sport", "blue_black", 2021, 270_000, 135)
car5 = Auto("Kia", "K6", "Gray", 2023, 130_000, 120, True)
car6 = Auto("BugaTTi", "Veron Sport", "blue_black", 2002, 240_000, 120, False)
car7 = Auto("Lambarghini", "Huragan", "dark_red_black", 2021, 230_000)

xMAxAutoStore = AutoStore("xMAxAutoStore")
xMAxAutoStore + car1
xMAxAutoStore.add_auto(car3, car6)
print(xMAxAutoStore)
xMAxAutoStore(car2)
# index = 1
# print(xMAxAutoStore[index])

MaxAuto = AutoStore("MaxAuto")
MaxAuto + car4
MaxAuto.add_auto(car7, car4, car5, car2)

print(MaxAuto)
MaxAuto(car7)
MaxAuto(car3)



print(xMAxAutoStore<MaxAuto)