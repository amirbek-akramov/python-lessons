"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""

# FileNotFoundError

filename = "file_name.txt"

try:
    with open(filename) as file:
        text = file.read()
        
except FileNotFoundError:
    print(f"'{filename}' not founded!")
    
# It's continue to work

import json # I don't write import in first line because this way is more comfortable now

files = ['JSON/employee.json','JSON/product.json','JSON/customer.json', "JSON/new_json.json", 'JSON/book.json', 'JSON/recipe.json']
for filename in files:
    try:
        with open(filename) as f:
            file_json = json.load(f)        
    
    except FileNotFoundError:
        # print(f"{filename} not found!") # or use "pass"
        pass
        
    else:
        print(file_json['name'])
