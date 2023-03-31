"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 18-dars: WHILE and Lists
sana: 04/03/2023
"""

# print("Let's create your friend list: ")
# names = []
# n=1

# while True:
#     question = f"{n} - friend's name: "
#     name = input(question)
#     names.append(name)
#     repeat = input("Any more (yes/no): ")
#     n+=1
#     if repeat != 'yes':
#         break
    
# print("Friends list: ")
# for friend in names:
#     print(friend.title())


"""
While with dictionaries

_______________________________________________________________________________
"""

# print("Collect informations about your friends: ")
# friends = {}

# while True:
#     question = "Your friend's" 
#     name = input(f"{question} name: ")
#     age = input(f"{question} age: ")
#     friends[name] = int(age)
    
#     answer = input("Any more (yes/no): ")
#     if answer == "no":
#         break
    
# for name, age in friends.items():
#     print(f"\nName: {name.title()}")
#     print(f"Age: {age}")


"""
"while" with "remove()"

_______________________________________________________________________________
"""

# cars = [
#     'bmw',
#     'lambarghini',
#     'bmw',
#     'toyota',
#     'nissan',
#     'bmw',
#     'merecedes',
#     'range rover',
#     'Škoda',
#     'audi'
# ]

# car = 'bmw'

# while car in cars:
#     cars.remove(car)
# print(cars)



"""
'While' with Dictionaries and Lists

_______________________________________________________________________________
"""

# students = [
#     "Johnson",
#     "Brown",
#     "James",
#     "William",
#     "Lucas",
#     "Henry",
#     "Jack",
#     "Michael"
# ]

# marked_students = {}

# while students:
#     student = students.pop()
#     mark = input(f"Mark of the {student.title()}: ")
#     print(f"{student.title()} was marked: {mark}")
#     marked_students[student] = int(mark)
# for learner, mark in marked_students.items():
#     print(f"{learner}: {mark}")



"""
Practise 1

_______________________________________________________________________________
"""

# orders = []

# while True:
#     order = input("Order the food ('exit' for stopping): ")
    
#     if order == "exit":
#         break

#     orders.append(order.lower())

# for order in orders:
#     print(order.title())
    
"""
Practise 2

_______________________________________________________________________________
"""

# products = {}

# while True:
#     order = input("('exit' for stopping) Product: ")
#     cost = input("('exit' for stopping) Cost ($): ")
    
#     if order == "exit" or cost == "exit":
#         break
    
#     products[order] = int(cost)
    
# for product, cost in products.items():
#     print(f"{product.title()} - {cost}$")


"""
Practise 3

_______________________________________________________________________________
"""

# products = {
#     "pizza":20,
#     "kebab":25,
#     "burger":3,
#     "cheeseburger":4,
#     "somsa":4,
#     "palow":30,
#     "fish":17,
#     "chips":7,
#     "potato fri":6
# }

# orders = []

# while True:
#     order = input("('exit' for stopping) Product: ")
    
#     if order == "exit":
#         break
    
#     orders.append(order.lower())
    
#     if order in products:
#         print(f"{order.lower()} - {products[order]}$")
    
#     else:
#         print("Sorry, We can't find this product!")

# for order in orders:       
#     if order in products:
#         print(f"{order.title()} - {products[order]}$")
#     else:
#         print(f"We can't find product: {order.title()}")