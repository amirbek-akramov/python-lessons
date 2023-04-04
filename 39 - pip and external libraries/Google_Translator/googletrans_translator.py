"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#39 - lesson: pip and external libraries
Date: 04/04/2023 // 7:45
"""

# pip install googletrans==3.1.0a0

from googletrans import Translator, LANGUAGES

translator = Translator() # Translator is class. 
# Now I create object from class Translator

text_uz = "Python - dunyodagi eng mashxur va eng oson dasturlash tillaridan bittasi"

# for translating use translate method
translated = translator.translate(text_uz)

# original text
print("Original: \n ", translated.origin)

# translated text
print("\nTranslated: \n ", translated.text)

# original text language
print("\nOriginal text language: \n ", translated.src)

""" For translating to other language use parameter 'dest' """

# From uzbek to russian
translated_uz_ru = translator.translate(text_uz, dest="ru")
print("\nFrom uzbek to russian: \n ", translated_uz_ru.text)

# From russian to english
translated_ru_en = translator.translate(translated_uz_ru.text)
print("\nFrom russian to english: \n ", translated_ru_en.text)

# English text for translating
text_en = "Java - Language for web, mobile, and enterprise software development."

# From english to uzbek
translated_en_uz = translator.translate(text_en, dest="uz")
print("\nFrom english to uzbek: \n ", translated_en_uz.text)

# From english to russian
translated_en_ru = translator.translate(text_en, dest="ru")
print("\nFrom english to russian: \n ", translated_en_ru.text)


"""
Mini project

_______________________________________________________________________________
"""
translated_words_phrases = {}

language = input("Translate to ('languages' to see all languages): ").lower()

if language != "languages":
    language_2th = input("Translate to second language('languages' to see all languages): ").lower()

if language == "languages" or language_2th == "languages":
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_name}: {lang_code}")
    language = input("Translate to: ").lower()
    language_2th = input("Translate to (second language): ").lower()

        

while True:
    word_phrase = input("Word or phrase (X for exit): ")
    translated_rl_lngg = translator.translate(word_phrase, dest=language)
    
    if word_phrase.lower() == translated_rl_lngg.text.lower():
        translated_rl_lngg = translator.translate(word_phrase, dest=language_2th)
    print(f"{word_phrase}: {translated_rl_lngg.text}")
    
    
    if word_phrase == "X" or word_phrase == "x":
        print("\nTranslated words:")
        for key, value in translated_words_phrases.items():
            print(f" {key} - {value}")
        break
    
    translated_words_phrases[word_phrase] = translated_rl_lngg.text
    