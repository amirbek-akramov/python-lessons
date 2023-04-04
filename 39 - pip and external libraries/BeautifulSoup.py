"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#39 - lesson: pip and external libraries
Date: 04/04/2023 // 11:00
"""

# BeautifulSoup not beautiful soup

import requests
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)


soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title") # extracting the title of informations

i = 0
while i != len(news):
    print(f"{i}.",news[i].text) # print the first news
    i += 1