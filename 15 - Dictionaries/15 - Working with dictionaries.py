"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 15-dars: Working with dictionaries
sana: 20/02/2023
"""

# items()

# student_0 = {
#     "name":"Amirbek",
#     "surname":"Akramov",
#     "age":13,
#     "faculty":"mathematics",
#     "course":4
# }

# print(student_0["age"])

# # items()

# print(student_0.items())
# print(student_0)


# for key, value in student_0.items():
#     print(f"KeyWord: '{key}'")
#     print(f"Value: '{value}'\n")


# telephones = {
#     "ali":"iphone X",
#     "temurbek":"galaxy S22 Ultra",
#     "amirbek":"telephone model P",
#     "hasan":"nokia 3310",
#     "someone":"xiomi X32"
# }


# for k, v in telephones.items(): # k = key, v = value
#     print(f"{k.title()}'s telephone is {v}")


"""
Only keys? Use method "keys()"

_______________________________________________________________________________
"""

# products = {
#     "beaf":"9$",
#     "coke":"1.3$",
#     "chips":"0.9$",
#     "apple":"0.5$",
#     "coconuts":"free",
#     "chocolate":"1.3$"
# }

# print(products.keys())


# for keys in products.keys():
#     print(f"KeyWord: {keys}")

"""
You can use "in" in order to "keys()"

_______________________________________________________________________________
"""



# products = {
#     "beaf":"9$",
#     "coke":"1.3$",
#     "chips":"0.9$",
#     "apple":"0.5$",
#     "coconuts":"free",
#     "chocolate":"1.3$"
# }

# print(products.keys())


# for product in products:
#     print(f"KeyWord: {product}")



#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



# products = {
#     "beaf":"9$",
#     "coke":"1.3$",
#     "chips":"0.9$",
#     "apple":"0.5$",
#     "coconuts":"free",
#     "chocolate":"1.3$"
# }

# needs = {
#     "beaf",
#     "crisps",
#     "coconut",
# }


# for product in products:
#     if product in needs:
#         print(f"{product.title()} {products[product]} so'm")


"______________________________________________________________________________"


# for thing in needs:
#     if thing not in products:
#         print(f"We can't find '{thing}'")


"""
You can use "sorted()" method for printing the dintionaries or list with ordered way

________________________________________________________________________________
"""


# products = {
#     "beaf",
#     "apple",
#     "coconuts",
#     "chips",
#     "coke",
#     "corn",
#     "television",
#     "clock",
#     "laptop",
#     "cake",
#     "chocolate",
#     "pizza",
#     "tomato",
#     "sousages",
#     "cream",
#     "ice cream",
#     "freezer",
#     "ruller",
# }

# print("Products that you can buy in our shop: ")
# for product in sorted(products):
#     print(product.title())




"""
Only values? Use method values()

_______________________________________________________________________________
"""


# products = {
#     "beaf":"9$",
#     "coke":"1.3$",
#     "chips":"0.9$",
#     "apple":"0.5$",
#     "coconuts":"free",
#     "chocolate":"1.3$"
# }

# print(products.values())

# print("This things costs: ")
# for product in products.values():
#     print(product)


"""
Use function "set()" for don't repeating the values or keys

"""

# telephones = {
#     "john":"iphone x",
#     "smith":"galaxy s21",
#     "agent":"huawei p30",
#     "alfred":"iphone x",
#     "conor":"galaxy s9",
#     "jake":"iphone x",
#     "kate":"galaxy s21",
# }

# for telephone in set(telephones.values()):
#     print(telephone)


"""
New information type "sets" like "lists"
If in "sets" there are two same words or number, "sets" delete one of them

______________________________________________________________________________
"""

# toys = {
#     3,
#     "lamp",
#     "car",
#     3,
# }

# print(type(toys))

# print(toys)


"""
Mini project from me

_______________________________________________________________________________
"""


# products = {
#     "beaf":"9$",
#     "coke":"1.3$",
#     "chips":"0.9$",
#     "apple":"0.5$",
#     "coconuts":"free",
#     "chocolate":"1.3$"
# }



# user = input("Command> ")

# if user.lower() == "product names":
#     for product in products.keys():
#         print(product.title())
    
# elif user.lower() == "costs":
#     for product in products.values():
#         print(product)
        
# elif user.lower() == "products":
#     for product, cost in products.items():
#         print(f"{product} - {cost}")
        
# elif user.lower() == "command":
#     print("product names \t\t\t\t\t costs \t\t\t\t\t products \t\t\t\t\t search product")

# elif user.lower() == "search product":
#     user2 = input("Product> ")
#     if user2.lower() in products.keys():
#         print(f"{user2.title()} - {products[f'{user2.lower()}']}")
#     else:
#         print("We don't have this product!")

# else:
#     print("We don't have this product!")





"""
Mini project from me

"Dictionary"

_______________________________________________________________________________
"""
# dictionary = []


# how_many = int(input("""How many words you want to write?
# >>> """))

# for dict in range(how_many):
#     dict1 = input("\nWord: ")
#     dict2 = input("Meaning: ")
#     dictionary.append(f"{dict1.lower()} - {dict2.lower()}")

# dictionary = set(dictionary)

# for word in sorted(dictionary):
#     print("\n",word.lower())






"""
HomeWork

_______________________________________________________________________________
"""


# python_dict = {
#     "if":"if conjunction (IN THAT SITUATION) A2. used to say that a particular thing can or will happen only after something else happens or becomes true: I'll pay you double if you get the work finished by Friday. We'll have the party in the garden if the weather's good.",
#     "else":"else. 1 of 2 adverb. ˈels. : in a different or additional manner or place or at a different time.",
#     "integer":"An integer (pronounced IN-tuh-jer) is a whole number (not a fractional number) that can be positive, negative, or zero. Examples of integers are: -5, 1, 5, 8, 97, and 3,043. Examples of numbers that are not integers are: -1.43, 1 3/4, 3.14",
#     "float":"It means that it gives 6-7 decimal digits precision. It is used if we want to use memory effectively because it takes less memory in comparison to double data type. To define a float value, we must use a suffix f or F. Its default value is 0.0f. By default, float numbers are treated as double in Java.",
#     "string":"String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are 'immutable' which means they cannot be changed after they are created.",
#     "for":"for loops are used when you have a block of code which you want to repeat a fixed number of times. The for-loop is always used in combination with an iterable object, like a list or a range. The Python for statement iterates over the members of a sequence in order, executing the block each time. Contrast the for statement with the ''while'' loop, used when a condition needs to be checked each iteration or to repeat a block of code forever",
#     "input":"The input() function allows a user to insert a value into a program. input() returns a string value. You can convert the contents of an input using any data type.",
#     "print":"The print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen.",
#     "dictionary":"A dictionary is a collection which is ordered*, changeable and do not allow duplicates. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.",
#     "tuple":"Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets." 
# }


# for key, value in sorted(python_dict.items()):
#     print(f"{key.title()} - {value}\n")



"""
HomeWork 2

_______________________________________________________________________________
"""

# countries = {
#     "france":"paris",
#     "uzbekistan":"tashkent",
#     "russia":"moskow",
#     "u.s.a":"washington d.c.",
#     "italy":"rim"
# }

# print("World countries: ")
# for country in sorted(countries):
#     print(country.title())
    

# print("\nThe capitals of countries: ")
# for country in sorted(countries.values()):
#     print(country.title())
    

# choose = input("Which country's capital would you like to know?: ").lower()

# if choose in countries:
#     print(f"{choose.title()}'s capital is {countries[choose].title()} ")

# else:
#     print("Sorry, we can't find information about this!!!")


"""
HomeWork 3

_______________________________________________________________________________
"""
foods = {
    "kebab":60_000,
    "steak":95_000,
    "sousages_in_cheese":35_000,
    "chicken":30_000,
    "tea":5_000,
    "bread":3_000,
    "palow":23_000,
    "somsa":9_000,
    "pasta":15_000,
}


print("You need to three foods: ")

orders = []

for q in range(3):
    orders.append(input(f"{q+1} - food: ").lower())

for order in orders:    
    if order in foods:
        print(f"{order.title()} costs {foods[order]} sum")
    else:
        print(f"There is no '{order}' in our menu")
