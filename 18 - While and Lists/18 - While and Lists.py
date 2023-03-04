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

print("Collect informations about your friends: ")
friends = {}
flag = True

while flag:
    question = "Your friend's" 
    name = input(f"{question} name: ")
    age = input(f"{question} age: ")
    friends[name] = int(age)
    
    answer = input("Any more (yes/no): ")
    if answer == "no":
        break
    
for name, age in friends.items():
    print(f"Name: {name.title()}")
    print(f"Age: {age}")
