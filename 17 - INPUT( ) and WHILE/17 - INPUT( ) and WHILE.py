"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 17-dars: INPUT() and WHILE
sana: 01/03/2023
"""

"""
If you want to collect info from user? Use "input()";

_______________________________________________________________________________
"""

# name = input("What's your name: ")
# question = f"Hello {name.title()}, how old are you: "
# age = input(question)
# age = int(age)
# height = input("How long are you (m): ")
# height = float(height)
# print("Thanks for information.")



"""
You can use "while" for repeating the some codes

_______________________________________________________________________________
"""

# number = 1

# while number<=5:
#     print(number, end=' ')
#     number+=1
# print("Programm is ended")


"""
With 'input()' and "while" you can ask how many repeat this code in action

_______________________________________________________________________________
"""

# print("This code print the square of numbers.")
# question = "Write random number: "
# question += "(Write 'exit' for stopping) "
# value = ''

# while value != 'exit':
#     value = input(question)
#     if value != 'exit':
#         print(float(value)**2)
# print("The programm was stopped!")


"""
Flag

_______________________________________________________________________________
"""

# print("This code print the square of numbers.") 
# question = "Write random number: "
# question += "(Write 'exit' for stopping) "
# flag = True
    
# while flag:
#     value = input(question)
#     if value == 'exit':
#         flag = False
#     else:
#         print(float(value)**2)
# print("The programm was stopped!")


"""
The one of the way for stopping the 'while' is "break"

_______________________________________________________________________________
"""



# print("This code print the square of numbers.") 
# question = "Write random number: "
# question += "(Write 'exit' for stopping) "
    
# while True: # infinity cycle
#     value = input(question)
#     if value == 'exit':
#         break # 'break' for stopping the infinity cycle
#     else:
#         print(float(value)**2)
# print("The programm was stopped!")


"""
However, you can use 'while' for 'for'

_______________________________________________________________________________
"""

# numbers = range(1,11)

# for number in numbers:
#     if number == 6:
#         break
#     print(f"{number}'s square equal to {number**2}")


"""
With 'continue' you can skip a step in some codes

_______________________________________________________________________________
"""

# numbers = list(range(1,11))

# for number in numbers:
#     if number == 5:
#         continue
#     print(f"{number}'s square equal to {number**2}")


"""
You can use 'continue' with while

_______________________________________________________________________________
"""

# number = 0

# while number<10:
#     number+=1
#     if number%2!=0:
#         continue
#     else:
#         print(number)


"""
Be careful from 'infinite loops'

_______________________________________________________________________________
!!! Dangerous !!!
:)

"""
# number = 0

# while number<10:
#     if number%2!=0:
#         continue
#     else:
#         print(number)


#### or ####

# number = 0
# while number<10:    
#     if number%2!=0:
#         continue
#     else:
#         print(number)
#     number += 1


#### or ####

# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

"""
Mini project from me

_______________________________________________________________________________
"""

# shop = {
#     "tomato":3,
#     "potato":3,
#     "carrot":4,
#     "onion":2,
#     "beaf":13,
#     "oil":6,
#     "sousage":8,
#     "chicken":9.4,
#     "cheese":6.5,
#     "mandarin":4.8,
#     "orange":7
# }

# products = []

# name = input("What's your name: ")

# print(f"Hello {name.title()}, Welcome to our shop. What would you like to buy?")
# flag = True


# while flag:
#     value = input("Write 'exit' for stopping>>> ")
#     if value != "exit":
#         products.append(value.lower())
#         for product in products:
#             if product.lower() in shop:
#                 print(f"{product.title()} - {shop[product]}$")
#             if product.lower() not in shop:
#                 print(f"There is no {product} in our shop!")
#     else:
#         print("\nYour list:")
#         products = set(products)
#         for product in products:
#             if product.lower() in shop:
#                 print(product.title())
#         flag = False
        
#         print("\nThe programm was stopped!")
    
