"""
# 14-dars: Dictionary (Lug'at)
sana: 17/02/2023
"""


# carDictionary = {
#     "model":"ferrari",
#     "color":"black"
# }

# print(carDictionary["model"])
# print(carDictionary["color"])


# someNumbers = {"num1":2, "num2":4}

# print(someNumbers["num1"] + someNumbers["num2"])




#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#



# en_uz = {
#     "support":"qo'llab quvvatlash",
#     "program":"dastur",
#     "advertisement":"reklama",
#     "choose":"tanlov",
#     "involve":"jalb qilmoq",
#     "toward":"tomon",
#     "underwent":"o'tkazgan",
#     "considered":"hisobga olinadi",
#     "satisfaction":"qoniqish",
#     "composed":"tuzilgan"
# }


# word = input("Search: ")

# print(f"{word} - {en_uz[word]}  ")

"""
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
"""


# products = {
#     "apple":"1.5$",
#     "banana":"1$",
#     "apricot":"2$",
#     "cheese":"3.4$",
#     "bread":"0.5$",
#     "sousage":"13$",
#     "beaf":"23$",
#     "chips":"5$",
#     "cocacola":"3.2$",
#     "pepsi":"2.3$"
# }


# choose = int(input("How many products you want to buy: "))

# for chose in range(choose):
#     product = input("Search: ").lower()
#     print(f"\n{product.title()} costs: {products[product]}")


"""
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
"""



"""
You can keep any types of information in 'dictionary'
"""

# student_0 = {"name":"Amirbek", "age":13,"birth_year":2009}

# print(f"Name: {student_0['name']}, \
# Age: {student_0['age']}, \
# Birth year: {student_0['birth_year']}")





"""
Adding the new key word and value
"""

# print(student_0)

# student_0['course'] = 4
# student_0['faculty'] = "informatics"
# student_0['name'] = "Anton"

# print(student_0)



# student_1 = {}

# student_1['name'] = "Amirbek"
# student_1['age'] = 13
# student_1['year'] = 2009

# print(student_1)
# print(f"Student: {student_1['name'].title()}, Birth year: {student_1['year']} and Age: {student_1['age']}")



"""
Updating the value
"""

# student_2 = {
#     "name":"Amirbek",
#     "age": 13,
#     "birth_year":2009,
#     "birth_date":"31 december",
#     "faculty":"sciense",
#     "course": 3
# }

# print(student_2)
# print(f"Student: {student_2['name'].title()}, Course: {student_2['course']} and Age: {student_2['age']}")

# student_2['age'] = 5
# student_2['name'] = "Temurbek"
# student_2['faculty'] = 'IT'
# student_2['course'] = 4


# print('\n',student_2)

# print(f"Student: {student_2['name'].title()}, Course: {student_2['course']} and Age: {student_2['age']}")




"""
Deleting the keyword and value
"""

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)


"""
Method: 'get()'
"""

# phones = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }


# phone = telefonlar['ali']
# print(f"Ali's phone {phone}")

# phone = telefonlar['hasan']
# print(f"Hasan's phone {phone}")


# phone = phones.get('hasan','We can\'t find this name!!!')
# print(phone)



# user = input("Who's telephone information you want to known?\n>>> ")
# print(phones.get(f"{user.lower()}", "In this moment, we can't find any information about this!"))


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#


# user = input("Who's telephone information you want to known?\n>>> ")
# print(phones.get(f"{user.lower()}"))


"""
Homework

_______________________________________________________________________________
"""

# dad = {
#    "name":"Sherzod",
#    "age":40,
#    "birth_year": 1983,
#    "job":"busness"
# }

# mom = {
#    "name":"Gulmira",
#    "age":37,
#    "birth_year": 1986,
#    "job":"scientist"
# }

# bro = {
#    "name":"Temurbek",
#    "age":14,
#    "birth_year": 2008,
#    "job":"Trader"
# }

# me = {
#    "name":"Amirbek",
#    "age":13,
#    "birth_year": 2009,
#    "job":"Programmer"
# }

# print(f"My father's name is {dad['name']}, his {dad['age']} years old, his birth year is {dad['birth_year']} and his jod is {dad['job']}\n")
# print(f"My mother's name is {mom['name']}, her {mom['age']} years old, her birth year is {mom['birth_year']} and her jod is {mom['job']}\n")
# print(f"My brother's name is {bro['name']}, his {bro['age']} years old, his birth year is {bro['birth_year']} and his jod is {bro['job']}\n")
# print(f"My name is {me['name']}, my {me['age']} years old, my birth year is {me['birth_year']} and my jod is {me['job']} ")




"""
Homework 2

_______________________________________________________________________________
"""


# foods = {
#     'ali':'palov',
#     'vali':'kebab',
#     'hasan':"steak",
#     'husan':"soup",
#     'olim':"samsa"
#     }

# food = foods['ali']
# print(f"Ali's favourite food is {food}")



"""
Homework 3

_______________________________________________________________________________
"""

# key_words = {
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


# user = input("Enter the key word: ")
# print(key_words.get(user, "We can't find the python defination of this word!"))



"""
Homework 4

_______________________________________________________________________________
"""


# key_words = {
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


# user = input("Enter the key word: ")

# if user in key_words:
#     print(key_words[user])
# else:
#     print(key_words.get(user, "We can't find the python defination of this word!"))
