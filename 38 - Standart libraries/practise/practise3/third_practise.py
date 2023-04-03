"Practise 3"

import datetime as dt

def age(year, month, day):
    birth_info = dt.date(year, month, day)
    now = dt.date.today()
    diference = now-birth_info
    month = diference/30
    year = month/12
    century = year/100
    print(f"{diference.days} days or about {month.days} months or {year.days} years or {century.days} century until your birthday")
    
year = int(input("Birth year: "))
month = int(input("Birth month (number): "))
day = int(input("Birth day (number): "))

age(year, month, day)