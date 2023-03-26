
from uuid import uuid4

class Car:
    __car_amount = 0
    def __init__(self, maded, model, color, year, cost, km=0):
        self.maded = maded
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost
        self.__km = km
        self.__id = uuid4()
        Car.__car_amount += 1

    @classmethod # decorative and functional methods
    def get_car_amount(cls): # cls = class
        return cls.__car_amount

    def add_km(self, km):
        self.__km += km if km >= 0 else print("You can't decrease drived km")

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id