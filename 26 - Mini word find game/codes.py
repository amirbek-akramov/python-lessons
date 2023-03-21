"""
Mini game "Find word if you can :)"
"""

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "_"
    return display_letter

def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    print(f"Мен {len(word)} хонали сўз ўйладимб топа оласизми?")
    
    while len(word_letters):
        print(display(user_letters, word))
        if len(user_letters):
            print(F"Олдинроқ йозган ҳарфларингиз: {user_letters}")
        
        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни олдин киритгансиз. Бошқа ҳарф киритинг :)")
            continue
        
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри")
        else:
            print("Бундай ҳарф йўқ")
        
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
        