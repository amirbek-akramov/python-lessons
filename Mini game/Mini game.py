"""
Mini game
"""
import random as rm


print("Write some notes for confortable playing!")
HARDNESS = input("Level (easy, normal, hard, titanium or unplayible): ").lower()
RANDOM_NUMBERS = int(input("Number for game: "))
CHANSES = 0

print("Random number is active!")



if HARDNESS == "easy":
    LEVEL = 25
    
elif HARDNESS == "normal":
    LEVEL = 50
    
elif HARDNESS == "hard":
    LEVEL = 100
    
elif HARDNESS == "titanium":
    LEVEL = 500
    
elif HARDNESS == "unplayible":
    LEVEL = 1000

else:
    print("This level isn't founded!")

number = rm.randint(0, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL)

while True:
    NUMBER2 = rm.randint(0, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL)
    
    if NUMBER2 < number:
        print(f"{NUMBER2} < random number")
        USER = int(input("Answer: "))
        CHANSES += 1
    
    if NUMBER2 > number:
        print(f"{NUMBER2} > random number")
        USER = int(input("Answer: "))
        CHANSES += 1
    
    if USER == number:
        print("Congratulations! Your answer is correct!!!")
        print(f"Correct answer: {USER}")
        print(f"For finding correct answer, you use: {CHANSES} chanses")
        CHANSES -= 1
        break

COMP_WANT = input("Let's play with computer (yes/no): ")

if COMP_WANT.lower() == "yes":
    COMP_CHANSES = 0
    print("Think some number and I will find the number that you think.")
    MAX = int(input("Maximum number: "))
    MIN = int(input("Minimum number: "))

    NUMBERS = list(range(MIN, MAX))

        # Need to write some codes for filter, for working normal.

    while True:
        ANSWER = input(f"{filter(NUMBERS < MAX, NUMBERS > MIN)} is my answer (True/False): ")
        COMP_CHANSES += 1
        
        if ANSWER.title() == "False":
            ANSWER = input(f"{filter(map(NUMBERS) < MAX, map(NUMBERS) > MIN)} is my answer (True/False): ")
            COMP_CHANSES += 1
        
        elif ANSWER.title() == "True":
            print(f"Computer find your number with: {COMP_CHANSES}")
            break

    if COMP_CHANSES < CHANSES:
        print(f"Computer win with less chanses: {COMP_CHANSES}")
    else:
        print(f"Player win with less chanses: {CHANSES}")

else:
    print("\n\nOur game is ended!!!")