from uuid import uuid4

class Car:
    __car_amount = 0

    def __init__(self, company, model, year, km=0, cost=None, extraTire=None):
        self.company = company
        self.model = model
        self.year = year
        self.__km = km
        self.__cost = cost
        self.__extraTire = extraTire
        self.__id = uuid4
        
        Car.__car_amount += 1

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company
    
    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def add_year(self):
        self.year += 1

    def set_year(self, year):
        self.year = year

    def get_id(self):
        return self.__id

    def get_km(self):
        return self.__km
    
    def add_km(self, __km):
        if __km>0:
            self.__km += __km
        else:
            raise ValueError(f"Don't add negative numbers to km: adding negative number {__km} to km")

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_extraTire(self):
        return self.__extraTire

    def get_info(self):
        info = f"Car information: \n Company: {self.company} \n Model: {self.model} \n Year: {self.year} "
        if self.__cost:
            info += f"\n Cost: {self.__cost}"
        elif self.__extraTire:
            info += f"\n Extra Tire: {self.__extraTire}"

        return info


car1 = Car("Toyota", "Corolla", 2021, 1000, 20000, False)
car2 = Car("Honda", "Civic", 2020, 5000, 15000, True)
car3 = Car("Ford", "Mustang", 2019, 8000)
car4 = Car("Chevrolet", "Camaro", 2018)

if __name__ == "__main__":
    print(car1.get_info())
    print(car2.get_info())
    print(car3.get_info())
    print(car4.get_info())