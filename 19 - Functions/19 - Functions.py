"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 19-dars: Functions (funktsiyalar)
sana: 06/03/2023
"""

"""
For creating the functions, you can use 'def'


Using:
    def name():
        #function

# Activate function like this ⬇:
name()
_______________________________________________________________________________

Example: 
"""

# def say_hello():
#     """Function that says 'Hello!'"""
#     print("Hello!")

# say_hello()

"""
Updating to next level

Using:
    
def name(something)
    #function 
    #using of 'something'
    
name('El macho')

# 'El macho' = something

_______________________________________________________________________________

Example:
"""

# def say_hello(name):
#     """Function that say hello with name"""
#     print(f"Welcome back to our hotel, Mr.{name.title()}")
    
# say_hello("Johnson") 
""" name = 'Johnson' """

### or ###

""" You can change string to input value like: """
# whats_your_name = input("What's your name: ")
# say_hello(whats_your_name)


""" It was ErroR when we don't give argumants: """
# say_hello()


'''
You need to give detailed information about your function 

_______________________________________________________________________________

def name()
    """ Detailed info """
'''

# print(say_hello.__doc__)

""" Some examples """

# print(print.__doc__)
# print(type.__doc__)
# print(input.__doc__)
# print(list.__doc__)
# print(tuple.__doc__)
# print(dict.__doc__)
# print(set.__doc__)
# print(int.__doc__)
# print(str.__doc__)
# print(float.__doc__)


"""
You can give more parameters than one

_______________________________________________________________________________

Example: 
"""

# def say_hello(firstName, secondName):
#     """ This function has two arguments that you need to give. 
#             Both of they are names of people."""
#     print(f"{firstName.title()} says 'hello' to {secondName.title()}")



# say_hello("Johnson", "Jack")


""" 
Be carefully with giving arguments

_______________________________________________________________________________

"""

# def age_calculator(name, birth_year):
#     """ Function that calculate the age of person """
#     print(f"{name.title()} is {2023-birth_year} years old.")
    

# age_calculator('Johnson', 1997)
# age_calculator(1997, 'Johnson')
    
""" You can use more easily way than this way 

Look at this:
"""

# age_calculator(name = "Johnson", birth_year = 1997)
# age_calculator(birth_year = 1997, name = "Johnson")


"""
You can give standard values on other hand, default values

_______________________________________________________________________________

Look at this:
"""

# def age(birthYear, nowYear = 2023):
#     """ The calculator of year """
#     print(f"Your are {nowYear-birthYear} years old.")

# # Both of this ways are right
# age(1997, 2050)
# age(1997)

"""
Unnecessary clone of function "print"

_______________________________________________________________________________
"""

# def console(something):
#     print(something)
    
# console("Unnecessary clone of the print using print")


"""
Practise 1

_______________________________________________________________________________
"""

# def name_age(age, name):
#     """ Function that can calculate the age """
#     print(f"Mr.{name.title()} your birth year: {2023-1-age}")
    
    
# NAME = input("Your name: ")
# AGE = int(input("Your age: "))

# name_age(age = AGE, name = NAME)

"""
Practise 2

_______________________________________________________________________________
"""

# def numberCollecter(number):
#     print(f"{number}'s square in {number**2}")
#     print(f"{number}'s cube is {number**3}")
    
# NUMBER = int(input("Number: "))

# numberCollecter(NUMBER)



"""
Practise 3

_______________________________________________________________________________
"""

# def anEvenNumber(number):
#     if (number%2) == 0:
#         print(f"{number} is even number")
#     else:
#         print("Please, enter even number!")

# NUMBER = int(input("Number: "))

# anEvenNumber(NUMBER)


"""
Practise 4

_______________________________________________________________________________
"""

# def bigOrSmall(first_number, second_number):
#     if first_number < second_number:
#         print(f"{first_number} < {second_number}")
        
#     elif first_number > second_number:
#         print(f"{first_number} > {second_number}")
        
#     else:
#         print(f"{first_number} = {second_number}")
        
# firstNumber = input("First number: ")
# secondNumber = input("Second number: ")

# bigOrSmall(first_number = firstNumber, second_number=secondNumber)


"""
Practise 5

_______________________________________________________________________________
"""


# def numbersLevel(x,y=2):
#     print(f"{x}**{y} = {x**y}")

# X = int(input("First number: "))
# Y = int(input("Second number: "))

# numbersLevel(x=X, y=Y)


"""
Practise 6

_______________________________________________________________________________
"""

# def numbersWithoutRemainder(NUMBER):
#     numbers = list(range(2,11))
#     for number in numbers:
#         if not NUMBER%number:
#             print(f"{NUMBER} is divisible to {number} without remainder")
        
# Number = int(input("Random number: "))

# numbersWithoutRemainder(Number)
