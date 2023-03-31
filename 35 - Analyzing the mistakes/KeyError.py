"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""

# KeyError

user = {"username":"anthon",
        "status":"admin",
        "email":"admin@anthon.python",
        "phone":"99897123456"}

key="tel"
try:
    print(f'User: {user[key]}')
except KeyError:
    print("KeyWord not found")