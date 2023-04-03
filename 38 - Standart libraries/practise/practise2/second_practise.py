"Practise 2"

import datetime as dt

ramazon_end = dt.date(2023,4,21)
now = dt.date.today()
diference = ramazon_end - now

print(f"{diference.days} days until to end of Ramadan")

qurbon_hayiti = dt.date(2023, 4, 23)
diference = qurbon_hayiti - now
print(f"{diference.days} days left for Eid al-Adha")
