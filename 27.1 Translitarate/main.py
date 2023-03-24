"""
GitHub:
27 - lesson: Telegram bot. Kiril to Latin or reverse
Date: 16.03.2023
"""

from transliterate import to_cyrillic, to_latin # imported the module that can translate cyrilic to latin or raverse

# question = int(input("To latin (1) or Cyrilic (0): "))

# if question:
#     text = input("Cyrillic text: ")
#     print("Latin text:", to_latin(text))

# elif not question:
#     text = input("Latin text: ")
#     print("Cyrillic text:", to_cyrillic(text))


"""
Second way

___________________________________________________________
"""

text = input("Text here: ")

if not text.isascii():
    print(f"Latin: {to_latin(text)}")

else:
    print(f"Cyrillic: {to_cyrillic(text)}")