"""
Mini game
"""
import random as rm


# Some questions

print("Write some notes for confortable playing!")
RANDOM_NUMBERS = int(input("Number for game: "))
HARDNESS = input("Level (easy, normal, hard, titanium or unplayible): ").lower()
CHANSES = 0

# Computer vs player

    # Selecting level of game

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
    print("This level not founded! Sets default level (normal)")
    LEVEL = 50
    

print("Random number is active!")

number = rm.randint(1, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL)

    # Main game

while True:
    NUMBER2 = rm.randint(1, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL)
   
    if NUMBER2 == number:
        NUMBER2 += rm.randint(1, 10)
        print(f"{NUMBER2} > random number")
        
    elif NUMBER2 > number:
        print(f"{NUMBER2} > random number")
    
    else:
        print(f"{NUMBER2} < random number")
    
    CHANSES += 1
    USER = int(input("Answer: "))
    
    if USER == number:
        print("Congratulations! Your answer is correct!!!")
        print(f"Correct answer: {USER}")
        print(f"For finding correct answer, you use: {CHANSES} chanses")
        break


# Player vs computer

COMP_WANT = input("Let's play with computer (yes/no): ")
input ("Press enter key for continue")


    # Some questions

if COMP_WANT.lower() == "yes":
    COMP_CHANSES = 0
    print("Think some number and I will find the number that you think.")

    LEVELS_COMP = [1,2,3,4]
    COMP_LEVEL_CHOISE = rm.choice(LEVELS_COMP)

    if COMP_LEVEL_CHOISE == 1:
        COMP_LEVEL_CHOISE = "easy"
        print(f"Computer choose {COMP_LEVEL_CHOISE} level")

    elif COMP_LEVEL_CHOISE == 2:
        COMP_LEVEL_CHOISE = "normal"
        print(f"Computer choose {COMP_LEVEL_CHOISE} level")

    elif COMP_LEVEL_CHOISE == 3:
        COMP_LEVEL_CHOISE = "hard"
        print(f"Computer choose {COMP_LEVEL_CHOISE} level")

    elif COMP_LEVEL_CHOISE == 4:
        COMP_LEVEL_CHOISE = "titanium"
        print(f"Computer choose {COMP_LEVEL_CHOISE} level")
    MAX = int(input("Maximum number: "))
    MIN = int(input("Minimum number: "))


    # Computer chosing the level

    NUMBERS = list(range(MIN, MAX))
    COMP_NUMBERS = []

    # Main game
    

    while True:
        COMP_CHOISE = rm.choice(NUMBERS)
        ANSWER = int(input(f"{COMP_CHOISE} is my answer (True = 1/False = 0): "))
        COMP_CHANSES += 1
        
        if not ANSWER:
            NUMBERS.remove(COMP_CHOISE)
            COMP_NUMBERS.append(COMP_CHOISE)
                
        if not NUMBERS:
            print("You don't think any number")
            break
            
        
        elif ANSWER:
            print(f"Computer find your number with: {COMP_CHANSES}")
            break

        
        def justice(WHITE_FLAG, COMP_CHANSES):
            for COMP_NUMBER in COMP_NUMBERS:
                if WHITE_FLAG == COMP_NUMBER:

                    print("I said this number.")
                    print("I use less chanses in real! :(")
                    break    

            return COMP_CHANSES



        if COMP_LEVEL_CHOISE == "easy":
            if COMP_CHANSES == 30:
                WHITE_FLAG = int(input("I can't find your number. What is number that you think: "))
                justice(WHITE_FLAG, COMP_CHANSES)
                break

        elif COMP_LEVEL_CHOISE == "normal":
            if COMP_CHANSES == 40:
                WHITE_FLAG = int(input("I can't find your number. What is number that you think: "))
                justice(WHITE_FLAG, COMP_CHANSES)
                break

        elif COMP_LEVEL_CHOISE == "hard":
            if COMP_CHANSES == 50:
                WHITE_FLAG = int(input("I can't find your number. What is number that you think: "))
                justice(WHITE_FLAG, COMP_CHANSES)
                break

        elif COMP_LEVEL_CHOISE == 'titanium':
            if COMP_CHANSES == 60:
                WHITE_FLAG = int(input("I can't find your number. What is number that you think: "))
                justice(WHITE_FLAG, COMP_CHANSES)
                break

            

        
    if COMP_CHANSES < CHANSES:
        print(f"\nComputer win with less chanses: {COMP_CHANSES}")
    elif COMP_CHANSES > CHANSES:
        print(f"\nPlayer win with less chanse (s): {CHANSES}")
    else:
        print(f"\nDraw, both of we have {CHANSES} used chanses")

else:
    print("\n\nOur game is ended!!! \n Thanks for playing!!!")