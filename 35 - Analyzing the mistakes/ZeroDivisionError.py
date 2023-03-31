"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""

# ZeroDivisionError

x,y = 5,10

try: # Never give up 😁
    math = y/(x-5)
except ZeroDivisionError: # if you want to give up 🤣
    print("ZeroDivisionError: division by zero \n Look at your code again and be more carefull from zero numbers.")
else:
    print(f"y/(x-5) = {math}")