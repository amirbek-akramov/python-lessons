"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#35 - lesson: Analyzing the mistakes
Date: 31/03/2023
"""

# IndexError

mevalar = ['olma','anor','anjir','uzum']
try:
    print(mevalar[7])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")