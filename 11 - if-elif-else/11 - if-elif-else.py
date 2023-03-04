"""
# 11-dars: if-elif-else
sana: 11/02/2023
"""

# You can write "elif" infinity times

# yosh = int(input("Yoshingiz nechida?\n>>> "))

# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5,000 so'm")
# elif yosh<=18:
#     print("Sizga kirish 7,000 so'm")
# elif yosh<=28:
#     print("Sizga kirish 8,000 so'm")
# elif yosh<89:
#     print("Sizga kirish 10,000 so'm")
# else:
#     print("Qariyalarni qadirlash yiliga murojat qiling")

"""
You can write "if-elif-else" with this easier way

_______________________________________________________________________________
"""

# yosh = int(input("Yoshingiz nechida?\n>>> "))

# if yosh<=4:
#     cost = 0
# elif yosh<=12:
#     cost = 5_000
# elif yosh<=18:
#     cost = 7_000
# elif yosh<=28:
#     cost = 8_000
# else:
#     cost = 10_000
    
# print(f"Sizga kirishga {cost} so'm")


"""
If you want to check two conditions you can use operator "and"

If you want to check a conditions or other condition you can use operator "or"



"or" and "and"

_______________________________________________________________________________
"""

# day = input("Bugun kun nima?\n>>> ")

# if day.lower() == "yakshanba" or day.lower() == "shanba":
#     print("Bugun dam olish kuni. Dam oling!")

# else:
#     print("Maktabga borish kerak. Maktab yoqmaydi! 😡")




#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



# day = input("What day is it today?\n>>> ")
# degree = float(input("What's the degree outside?\n>>> "))

# if (day.lower() == "yakshanba" or day.lower() == "shanba") and degree >= 30:
#     print("Let's go to swimming!")

# elif (day.lower() == "yakshanba" or day.lower() == "shanba") and degree < 30:
#     print("Let's stay at home!")

# else:
#     print("Tashqorni necha gradus bo'sayam ishga borish kerak")


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



"""
Information type: Boolean

Boolean: "True" or "False"

_______________________________________________________________________________
"""


# narh = 15_000 #mijoz 15ming so'mga taom oldi
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10_000

# elif choy or salat:
#     narh = narh + 5_000
    
# print(f"Jami narh {narh} so'm")


"""
Chacking all conditions

write without "elif"
_______________________________________________________________________________
"""

# narh = 0

# shorva = True
# salat = False
# non = True
# kompot = True
# assorti = True

# if shorva:
#     print("Mijoz sho'rva oldi.")
#     narh = narh + 15_000
    
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5_000
    
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 10_000
    
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 10_000

# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 60_500
    
    
# print(f"Jami narh {narh} so'm")


"""
You can use "1" in order to "True"
and "0" in order to "False"
"""


# narh = 0

# shorva = 1
# salat = 1
# non = 1
# kompot = 1
# assorti = 0

# if shorva:
#     print("Mijoz sho'rva oldi.")
#     narh = narh + 15_000
    
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5_000
    
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 10_000
    
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 10_000

# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 60_500
    
    
# print(f"Jami narh {narh} so'm")
    

"""
Use "in" to search string in list

_______________________________________________________________________________
"""

# menu = [
#     "manti",
#     "somsa",
#     "sho'rva",
#     "qozonkabob",
#     "norin",
#     "shashlik",
#     "ko'zasho'rva",
#     "kosasomsa"
# ]

# search = "go'sht" in menu

# print(search)



#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#


# menu = [
#     "manti",
#     "somsa",
#     "sho'rva",
#     "qozonkabob",
#     "norin",
#     "shashlik",
#     "ko'zasho'rva",
#     "kosasomsa"
# ]

# food = input("Nima ovqat yeysiz?\n>>> ")

# if food.lower() in menu:
#     print("Buyurmangiz qabul qilindi.")

# else:
#     print("Afsuski bizda bunday ovqat yo'q")



"""
Reverse type of operator "in": "not in"

_______________________________________________________________________________
"""

# menu = [
#     "manti",
#     "somsa",
#     "sho'rva",
#     "qozonkabob",
#     "norin",
#     "shashlik",
#     "ko'zasho'rva",
#     "kosasomsa"
# ]

# food = input("Nima ovqat yeysiz?\n>>> ")

# if food.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q")

# else:
#     print("Buyurmangiz qabul qilindi.")



"""
Mini project

_______________________________________________________________________________
"""


menu = [
    "manti",
    "somsa",
    "sho'rva",
    "qozonkabob",
    "norin",
    "shashlik",
    "ko'zasho'rva",
    "kosasomsa"
]

orders = []

numberOfOrders = int(input("Nechta buyurtma qilmoqchisiz?\n>>> "))

if numberOfOrders: # you can not write this "if"
    for order in range(numberOfOrders):
        order = orders.append(input("Qanday taom buyurtma qilasiz?\n>>> "))
        
    
    for food in orders:
        if food in menu:
            print(f"Buyurtmangiz: '{food}' qabul qilindi. ")
            
        else:
            print(f"Kechirasiz menuda {food} yo'q")

else:
    print("Biror nima buyurtma qilmaysizmi?")




"""
                        Homeworks

_______________________________________________________________________________
"""


# juftSon = int(input("Juft son kiriting: "))
# juft = juftSon % 2

# if juft > 0:
#     print(f"Bu juft son emas. {juftSon}")
    
# else:
#     print("Rahmat!")





#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



# age = int(input("Please write your age: "))

# if age <= 4 or age >= 60:
#     narh = 0
# elif age < 18:
#     narh = 10_000
# else:
#     narh = 20_000
    

# print(f"Sizga muzeyga kirish {narh} so'm")





#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



# firstNumber = float(input("Write first number: "))
# secondNumber = float(input("Write second number: "))


# if firstNumber == secondNumber:
#     print(f"{firstNumber} = {secondNumber}")

# elif firstNumber < secondNumber:
#     print(f"{firstNumber} < {secondNumber}")


# else:
#     print(f"{firstNumber} > {secondNumber}")






#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



# products = [
#     "pomidor",
#     "shaftoli",
#     "bodring",
#     "piyoz",
#     "kartoshka",
#     "kolbasa",
#     "sosiska",
#     "apelsin",
#     "mandarin",
#     "limon"
# ]

# marketBag = []
# thingsThatTheyBuy = int(input("Nechta narsa sotib olasiz?\n>>> "))

# for things in range(thingsThatTheyBuy):
#     marketBag.append(input(f"Savatga {things+1}-mahsulotni qo'shing: "))
    
# if marketBag:    
#     for product in marketBag:
#         if product in products:
#             print(f"\nBizning do'konda '{product}' bor")
    
#         else:
#             print(f"\nMahsulot '{product}' do'konimizda yo'q")

# else:
#     print("Savatingiz bo'sh")





#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#





# products = [
#     "pomidor",
#     "shaftoli",
#     "bodring",
#     "piyoz",
#     "kartoshka",
#     "kolbasa",
#     "sosiska",
#     "apelsin",
#     "mandarin",
#     "limon"
# ]

# marketBag = []
# haveProducts = []
# haveNotProducts = []
# thingsThatTheyBuy = int(input("Nechta narsa sotib olasiz?\n>>> "))

# for things in range(thingsThatTheyBuy):
#     marketBag.append(input(f"Savatga {things+1}-mahsulotni qo'shing: "))
    
# if marketBag:
#     for product in marketBag:
#         if product in products:
#             haveProducts.append(product)
    
#         else:
#             haveNotProducts.append(product)
        
#     if haveNotProducts:
#         print("\nDo'konimizda manabu productlar yo'q:")
#         for haveNotProduct in haveNotProducts:
#             print(haveNotProduct)
#     else:
#         print("\nSiz so'ragan barcha mahsulotlar do'konimizda bor")
     

# else:
#     print("Savatingiz bo'sh")





#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#





# logins = [
#     "anvar",
#     "admin",
#     "umar",
#     "hoshim",
#     "akbar"
# ]


# newLogin = input("Yangi login tanlang: ")

# if newLogin.lower() in logins:
#     print(f"Yangi login tanlang. Login '{newLogin}' band  qilingan")
    
# else:
#     print(f"Xush kelibsiz {newLogin}!")







#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#





# number = int(input("Istalgan son yozing: "))

# for n in range(2 ,11):
#     if not number%n:
#         print(f"{number} soni {n}ga qoldiqsiz bo'linadi")