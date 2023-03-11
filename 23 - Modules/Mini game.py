"""
Mini game
"""
import random as rm


# randint()
# random integer

RANDOM_NUMBERS = int(input("Average number for game: "))

print("Random number is active!")
number = rm.randint(0, RANDOM_NUMBERS+RANDOM_NUMBERS+50)

while True:
    NUMBER2 = rm.randint(0, RANDOM_NUMBERS+RANDOM_NUMBERS+50)
    
    if NUMBER2 < number:
        print(f"{NUMBER2} < random number")
        USER = int(input("Answer: "))
    
    if NUMBER2 > number:
        print(f"{NUMBER2} > random number")
        USER = int(input("Answer: "))
    
    if USER == number:
        print(f"Answer is correct: {USER}")
        break

