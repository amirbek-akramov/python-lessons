"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#38 - lesson: Standart modules of python
Date: 03/04/2023 // 8:10
"""
import pprint
import json

# pprint

file_name = "JSON/json_file.json"

with open(file_name) as json_file:
    person = json.load(json_file)

print("Without pprint: ")
print(person)

print("\n\nWith pprint: ")
pprint.pprint(person)