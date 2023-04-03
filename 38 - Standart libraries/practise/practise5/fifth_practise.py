"Practise 5"

import re

text = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:
https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar
va metodlarini tekshiruvchi dastur yozishni o'rganamiz.
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

def pop_urls(string):
    pattern = re.compile(r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?')
    finding = re.findall(pattern, string)
    if finding:
        print(finding)
    else:
        print("URL not found!")
        
pop_urls(text)