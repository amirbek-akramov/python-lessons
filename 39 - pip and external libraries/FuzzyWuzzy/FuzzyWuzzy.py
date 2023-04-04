"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#39 - lesson: pip and external libraries
Date: 04/04/2023 // 11:23
"""

from fuzzywuzzy import fuzz, process
from wordsmodule import words
import random


# text = "салом"
# matches = process.extract(text, words, limit = 5)
# print(matches)

text = "талба"
match_word = process.extractOne(text,words)
print(match_word)




"""
Mini project
"""


# choice_word = random.choice(words)

# i=0
# print("Сўзлар рўйхати: ")
# for word in words:
#     if (fuzz.ratio(choice_word, word)) >= 60:
#         i+=1
#         print(f"{i}. {word}")

# main_word = input("Сўз киритинг: ")



# difference = fuzz.ratio(main_word, choice_word)
# print(f"{difference}% тўгри")

# while difference!=100:
#     main_word = input("Сўз киритинг: ").lower()
    
#     difference = fuzz.ratio(main_word, choice_word)
#     print(f"{difference}% тўгри")

#     if main_word == "x":
#         print(f"Сўзни топа олмадигиз! Сўз '{choice_word}' еди.")
#         break
    

