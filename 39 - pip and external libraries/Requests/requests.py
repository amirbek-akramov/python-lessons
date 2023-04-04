"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#39 - lesson: pip and external libraries
Date: 04/04/2023 // 9:40
"""

# Requests

import requests
# from pprint import pprint

# website = "https://kun.uz/news/main"

# r = requests.get(website)

# pprint(r.text)


# restcountries API

# country = input("Information about country: ").title()
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]

# # print(r_json.keys())

# print(r_json['capital'])

"""
Mini project
"""

from googletrans import Translator, LANGUAGES

language = input("Advice language: ")

url = "https://api.adviceslip.com/advice"

if language != "languages":    
    how_many = int(input("How many advices do you want to take?\n>>> "))


translator = Translator()


if language == "languages":
    for lan_code, lan_name in LANGUAGES.items():
        print(f"{lan_name}: {lan_code}")
    language = input("Advice language: ")
    how_many = int(input("How many advices do you want to take?\n>>> "))
        

i = 0
while i != how_many:
    r = requests.get(url)
    i += 1
    print(f"{i}. ",translator.translate(r.json()['slip']['advice'], dest=language).text)