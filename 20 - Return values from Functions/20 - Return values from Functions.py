"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 20-dars: Return values from functions
sana: 09/03/2023
"""

"""
Use 'return' for saving the variables

_______________________________________________________________________________

1 - way (without 'return')
"""



"""
2 - way (with 'return')
"""

# def create_full_name(name, surname):
#     """Full name returner from function"""
#     full_name = f"{name} {surname}"
#     return full_name

# """ You can use this variable more time"""

# creater_of_full_name = create_full_name(name = "John", surname = "Johnson")


# """ Where you can use this """

# student1 = create_full_name(name = "John", surname = "Johnson")
# student2 = create_full_name(name = "Jack", surname = "Jackson")
# student3 = create_full_name(name = "Nick", surname = "Nickson")
# student4 = create_full_name(name = "William", surname = "Williamson")

# print(f"The students that didn't come to extra lesson: {student1}, {student2}, {student3}, {student4}")



"""
!!! More harder !!!

_______________________________________________________________________________
"""



# def create_full_name(name, surname, father_name=""):
#     """Full name returner from functions"""
#     if father_name:
#         full_name = f"{surname} {name} {father_name}"
#     else:
#         full_name = f"{name} {surname}"
#     return full_name.title()

# student1 = create_full_name("Jack", "Johnson")
# student2 = create_full_name("Jack", "Johnson", "John")

# print(f"Our active students: {student1} and {student2}")


"""
You can return more variables useing "return".

_______________________________________________________________________________

For example:
"""

# def auto_info(company, model, color, auto_type, year, costs=None):
#     car = {
#         "company":company,
#         "model":model,
#         "color":color,
#         "type":auto_type,
#         "year":year,
#         "cost":costs
#     }
#     return car


# car1 = auto_info("BMW", "X7", "black", "manual", 2005,88_000_000)
# car2 = auto_info("Nissan", "Skyline", "white", "auto", 2009, 120_000_000)
# car3 = auto_info("Lambarghini", "Huragan", "gray", "auto", 2013)


# print("Online shop's available cars: ")
# cars = [car1, car2, car3]
# for car in cars:
#     if car["cost"]:
#         cost = car["cost"]
#     else:
#         car['cost'] = "unknown"
#     print(f"{car['color']}, {car['company']} {car['model']} Cost: {car['cost']}")


"""
Clone of "range()" function

_______________________________________________________________________________
"""

# def intermediate(min,max, step=None):
#     numbers = []
#     while min<max:
#         numbers.append(min)
#         if step:
#             min += step
#         else:
#             min += 1
#     return numbers
    
# print(intermediate(0, 150,15))

### or ###
### more short way ###

# def intermediate(min,max, step=1): 
#     numbers = []
#     while min<max:
#         numbers.append(min)
#         min += step
#     return numbers
    
# print(intermediate(0, 150))


"""
_______________________________________________________________________________
"""

# def auto_info(company, model, color, auto_type, year, costs=None):
#     car = {
#         "company":company,
#         "model":model,
#         "color":color,
#         "type":auto_type,
#         "year":year,
#         "cost":costs
#     }
#     return car

# cars = []

# while True:
#     company = input("Company: ")
#     model = input("Model: ")
#     color = input("Color: ")
#     auto_type = input("Type: ")
#     year = int(input("Year: "))
#     costs = int(input("Cost: "))
    
#     cars.append(auto_info(company.lower(), model.lower(), color.lower(), auto_type.lower(), year, costs))
    
#     answer = input("Do you want to add more (yes/no): ")
#     if answer != 'yes':
#         break

# print("Online shop's available cars: ")
# for car in cars:
#     if car["cost"]:
#         cost = car["cost"]
#     else:
#         car['cost'] = "unknown"
#     print(f"Color: {car['color'].title()}, {car['company'].title()} {car['model'].title()} Cost: {car['cost']}$")


"""
Practise 1,2

_______________________________________________________________________________
"""

# def client_info(name, surname, birth_year, birth_place, email=None, telephone_number=None):
#     client = {
#         "name":name,
#         "surname":surname,
#         "birth_year":birth_year,
#         "birth_place":birth_place,
#         "email":email,
#         "telephone_number":telephone_number
#     }
#     return client

# clients = []

# while True:
#     name = input("Name: ")
#     surname = input("Surname: ")
#     birth_year = int(input("Birth year: "))
#     birth_place = input("Birth place: ")
#     email = input("E-mail: ")
#     telephone_number = input("Telephone number: ")
    
#     clients.append(client_info(name.lower(), surname.lower(), birth_year, birth_place.lower(), email.lower(), telephone_number))

#     answer = input("More clients (yes/no): ")
#     if answer != 'yes':
#         break
    
# print("Clients' information: ")

# for client in clients:
#     if not client['email']:
#         client['email'] = "Not Given"
#     if not client['telephone_number']:
#         client['telephone_number'] = "Not Given"
    
#     print(f"{client['surname'].title()} {client['name'].title()}, Age: {2023 -1- client['birth_year']}. Email:{client['email']},  Tel:+{client['telephone_number']}")




"""
Practise 3

_______________________________________________________________________________
"""

# def biggest(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# print(biggest(99,544,16))

        




"""
Practise 4

_______________________________________________________________________________
"""

# def circle_info(radius, pi = 3.14159):    
#     circle = {
#         "radius":radius,
#         "diametr":radius*2,
#         "peremetr": 2 * radius * pi,
#         "surface": pi * radius ** 2,
#     }
#     return circle

# radius = int(input("Radius: "))

# circle_info(radius)


"""
Practise 5

_______________________________________________________________________________
"""


# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# print(tub_sonlar_top(0, 1000))


"""
Practise 6

_______________________________________________________________________________
"""

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))