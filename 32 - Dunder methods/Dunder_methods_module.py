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

    def get_extra_tire(self):
        return self.__extraTire
    
    def exrta_tire(self):
        self.__extraTire if not self.__extraTire else not self.__extraTire

    def get_km(self):
        return self.__km
    
    def add_km(self):
        self.__km += 1

    def set_km(self, km):
        self.__km = km

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

    def __call__(self, *autos):
        if autos:
            for auto in autos:
                if isinstance(auto,Auto):
                    if auto in self.auto_amount:
                        print(f"Auto's informations: \n Company: {auto.company} \n Model: {auto.model} \n Color: {auto.color.upper()} \n Year: {auto.year}")

                    else:
                        print(f"\nThis method works with autos that have in {self.name}\n")

                else:
                    print("This method works only with 'Auto' class")
        
        else: 
            print("\nTypeError: AutoStore.__call__() missing arguments: *autos\n")
        
    
    def add_auto(self, *autos):
        if autos:
            for auto in autos:
                if isinstance(auto,Auto):
                    self.auto_amount.append(auto)
                else:
                    print("This method works only with 'Auto' class")
        
        else: 
            print("\nTypeError: AutoStore.__call__() missing arguments: *autos\n")

    def __add__(self, auto):
        if isinstance(auto,Auto):
            self.auto_amount.append(auto)
        else:
            print("This method works only with 'Auto' class")

    def __sub__(self, auto):
        if auto in self.auto_amount:
            if isinstance(auto,Auto):
                self.auto_amount.remove(auto)
            else:
                print("This method works only with 'Auto' class")
        else:
            print("You can remove only the autos that added")

    def get_cars_info(self):
        print("\nAll autos in our story: \n")
        for auto in self.auto_amount:
            print(auto, end="\n\n")


    def __getitem__(self, index):
        return self.auto_amount[index]
        
    def __setitem__(self, index, value):
        self.auto_amount[index] = value
        
    def __repr__(self):
        return f"\n{self.name} auto store have {len(self.auto_amount)} auto(s)."

    def __lt__(self, y):
        return len(self.auto_amount) < y
    
    def __le__(self, y):
        return len(self.auto_amount) <= y
    
    def __gt__(self, y):
        return len(self.auto_amount) > y
    
    def __ge__(self, y):
        return len(self.auto_amount) >= y
    
    def __eq__(self, y):
        return len(self.auto_amount) == y
    
    def __ne__(self, y):
        return len(self.auto_amount) != y