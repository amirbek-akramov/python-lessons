"""
# 06-dars: Numbers
sana: 23/01/2023
"""

a = 5 # Int (Integer)
b = 5.5 # Float (Floating point number)

print(type(a))

# aholi_soni = 7_569_538_679
# print("Aholi soni:", aholi_soni)

# x, y, z = 13.5, 10, -13

# c = x*y

# print(c)

# d=100/2
# print(d)


# _____________________________________________________________________________

# radius = 20
# PI = 3.14159
# diametr = 2*radius

# print("Aylana uzunligi =", PI*diametr)


# _____________________________________________________________________________
"""
       str = string, str() transforms everything to string
"""
    

# name = "Amirbek"
# age = 13

# age = str(age)

# nameAndAge = name + " " + age + ' yoshda'
# nameAndAge = name + " " + f"{age}"  + ' yoshda'

"""
Write this for more correct code
"""

# nameAndAge = name + " " + str(age) + " yoshda"

# print(nameAndAge)

# _____________________________________________________________________________
    
"""
        int = integer, int() transforms string numbers to integer or number
"""

# firstNumber = 7
# secondNumber = "8"

# secondNumber = int(secondNumber)

# numbers = firstNumber + secondNumber

# print(numbers)

# _____________________________________________________________________________

# birthday = input("Tug'ilgan yilingizni kiriting: ")
# month = input("Tug'ilgan oyingizni kiriting: ").title()
# age = 2023-int(birthday)

# if month == "January":
#     month = 1
    
# elif month == "Febuary":
#     month = 2
    
# elif month == "March":
#     month = 3
    
# elif month == "April":
#     month = 4
    
# elif month == "May":
#     month = 5
    
# elif month == "June":
#     month = 6
    
# elif month == "July":
#     month = 7
    
# elif month == "Ougust":
#     month = 8
    
# elif month == "September":
#     month = 9
    
# elif month == "Octomber":
#     month = 10
    
# elif month == "November":
#     month = 11
    
# else:
#     month = 12
    
# ageMonth = 12-month
    
# print(f"Sizning yoshingiz {age}da ekan va {ageMonth} oy ekan siz.")

# _____________________________________________________________________________
    
"""
        float = float point number, float() transforms string float numbers to float
"""

# birthday = int(input("Nechanchi yil tugilgsnsiz? \n>>> "))

# birthday = 2023-birthday

# print("Sizni yoshingiz " + str(birthday) + "da ekan.")


# integer = int("23")
# float_point_number = float("23")
# string = str(12)

# _____________________________________________________________________________

"""
                    Homework
"""

#                              №1

# number = int(input("Istalgan son kiriting: \n>>> "))
# vadrat = int(input("Shu sonni nechanchisini topaylik: \n>>> "))

# vadratNumber = number**vadrat


# print(str(number) + "ning" + " " + str(vadrat) + "nchi darajasi" + " " + str(vadratNumber) + " bo'ladi")


#                              №2

# age = int(input("Necha yoshda siz: "))

# age = 2023-age

# print("Siz " + str(age) + " yilda tug'ilgan ekansiz.")


#                              №3

# numberFirst = float(input("Istalgan sonningizni kitiring: "))
# numberSecond = float(input("Istalgan ikkinchi sonningizni kitiring: "))

# plus = float(numberFirst+numberSecond)
# minus = float(numberFirst-numberSecond)
# kopaytir = float(numberFirst*numberSecond)
# bol = float(numberFirst/numberSecond)

# print(f"{numberFirst} + {numberSecond} = {plus}")
# print(f"{numberFirst} - {numberSecond} = {minus}")
# print(f"{numberFirst} * {numberSecond} = {kopaytir}")
# print(f"{numberFirst} / {numberSecond} = {bol}")
