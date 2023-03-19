# # Mini game tests

# """
# Mini game
# Do more chanses to computer
# """
# def mini_game():
#     while True:
#         import random as rm
        
        
#         # Some questions
        
#         print("Write some notes for confortable playing!")
#         RANDOM_NUMBERS = int(input("Number for game: "))
#         HARDNESS = input("Level (easy, normal, hard, titanium or unplayible): ").lower()
#         CHANSES = 0
#         LEVEL = 0
        
#         # Computer vs player
        
#             # Selecting level of game
        
#         if HARDNESS == "easy":
#             LEVEL = 25
            
#         elif HARDNESS == "normal":
#             LEVEL = 50
            
#         elif HARDNESS == "hard":
#             LEVEL = 100
            
#         elif HARDNESS == "titanium":
#             LEVEL = 500
            
#         elif HARDNESS == "unplayible":
#             LEVEL = 1000
        
#         else:
#             print("This level not founded! Sets default level (normal)")
#             LEVEL = 50
            
        
#         print("Random number is active!")
        
#         comp_number = rm.randint(1, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL)
        
#             # Main game
        
#         while True:
#             NUMBER2 = rm.randint(1, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL)
           
#             if NUMBER2 == comp_number:
#                 NUMBER2 += rm.randint(1, 10)
#                 print(f"{NUMBER2} > random number")
                
#             elif NUMBER2 > comp_number:
#                 print(f"{NUMBER2} > random number")
            
#             else:
#                 print(f"{NUMBER2} < random number")
            
#             CHANSES += 1
#             USER = int(input("Answer: "))
            
#             if USER == comp_number:
#                 print("Congratulations! Your answer is correct!!!")
#                 print(f"Correct answer: {USER}")
#                 print(f"For finding correct answer, you use: {CHANSES} chanses")
#                 break
        
        
#         # Player vs computer
        
#         COMP_WANT = input("Let's play with computer (yes/no): ")
        
        
#             # Some questions
        
#         if COMP_WANT.lower() == "yes":
#             COMP_CHANSES = 0
#             print("I will play in same rules as you! :)")
#             print(f"On other hand, {HARDNESS} level with number {RANDOM_NUMBERS}")
#             print(f"Think any number untill {RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL}")
#             input ("Press enter key for continue")
        
        
#             NUMBERS = list(range(1, RANDOM_NUMBERS+RANDOM_NUMBERS+LEVEL))
#             COMP_NUMBERS = []
        
#             # Main game
            
        
#             while True:
#                 COMP_CHOISE = rm.choice(NUMBERS)
#                 ANSWER = input(f"{COMP_CHOISE} is my answer (True = t/)): ")
#                 COMP_CHANSES += 1
                
                    
                
                
#                 if not NUMBERS:
#                     print("You don't think any number")
#                     break
                    
                
#                 elif ANSWER.lower() == "t":
#                     print(f"Computer find your number with: {COMP_CHANSES}")
#                     break
        
                
#                 def justice(WHITE_FLAG, COMP_CHANSES):
#                     for COMP_NUMBER in COMP_NUMBERS:
#                         if WHITE_FLAG == COMP_NUMBER:
        
#                             print("I said this number.")
#                             print("I use less chances in real! :(")
#                             break    
        
#                     return COMP_CHANSES
        
        
                
#             if COMP_CHANSES < CHANSES:
#                 print(f"\nComputer win with less chances: {COMP_CHANSES}")
#             elif COMP_CHANSES > CHANSES:
#                 print(f"\nPlayer win with less chance (s): {CHANSES}")
#             else:
#                 print(f"\nDraw, both of we have {CHANSES} used chances")
        
#         else:
#             print("\n\nOur game is ended!!! \n Thanks for playing!!!")
            
            
#         PLAY_AGAIN = int(input("Do you want to play again? (No I have some works (0) / Yes definately (1)): "))
        
#         if not PLAY_AGAIN:
#             break
        
# mini_game()