class Auto:
    __auto_amount = 0

    def __init__(self, company, model, color, year, cost, __km=0, __extraTire=True):
        self.company = company
        self.model = model
        self.color = color
        self.year = year
        self.cost = cost
        self.__km = __km
        self.__extraTire = __extraTire
        Auto.__auto_amount += 1

    def __repr__(self):
        return f"Auto's informations: \n Company: {self.company} \n Model: {self.model} \n Color: {self.color.upper()} \n Year: {self.year}"
    
    def __lt__(self, y):
        return self.cost < y
    
    def __le__(self, y):
        return self.cost <= y
    
    def __gt__(self, y):
        return self.cost > y
    
    def __ge__(self, y):
        return self.cost >= y
    
    def __eq__(self, y):
        return self.cost == y
    
    def __ne__(self, y):
        return self.cost != y

    

class AutoStore:
    def __init__(self, name):
        self.name = name
        self.auto_amount = []
    
    def add_auto(self, *autos):
        for auto in autos:
            if isinstance(auto,Auto):
                self.auto_amount.append(auto)
            else:
                print("This method works only with 'Auto' class")

    def get_cars_info(self):
        print("\nAll autos in our story: \n")
        for auto in self.auto_amount:
            print(auto, end="\n\n")

    def __getitem__(self, index):
        return self.auto_amount[index]
        
    def __setitem__(self, index, value):
        self.auto_amount[index] = value
    def __repr__(self):
        return f"\n\nWe have {len(self.auto_amount)} autos in store"
