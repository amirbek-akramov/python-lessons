"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#36 - lesson: Checking the functions
Date: 1/04/2023
"""

def get_full_name(name, surname, father = ""):
    return f"{name} {father} {surname}".title() if father else f"{name} {surname}".title()