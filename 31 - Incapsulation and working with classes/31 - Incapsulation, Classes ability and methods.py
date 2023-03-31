"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#31 - lesson: Incapsulation, Classe's ability and methods
Date: 25/03/2023
"""
from Module_helper import Car

car1 = Car("Nissan", "SkyLine", "blue", 2018, 190_000, 150)
car2 = Car("BMW", "Model R7", "black", 2008, 195_000, 100)
car3 = Car("Kia", "K6", "white", 2010, 156_000, 50)
car4 = Car("Kia", "K7", "gray", 2011, 110_000, 50_000)
car5 = Car("Lambarghini", "Aventador", "yellow", 2013, 210_000, 150_000)
car6 = Car("BugaTTi", "Veron Sport", "red", 2015, 230_000, 510_000)
car7 = Car("Mitsubishi Motors", "Pajero Sport", "black", 2018, 120_000, 150_000)
car8 = Car("Mitsubishi Motors", "Pueroja Sport", "white", 2012, 115_000, 150_000)

print(Car.get_car_amount())
