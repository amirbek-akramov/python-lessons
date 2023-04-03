"Practise 1"

import datetime as dt

now = dt.date.today()
day = now.day
month = now.month
year = now.year
two_weeks = 14

print(f"\n\nToday's date: {now}\n")

i = 0
while i!=100:
    i += 1
    day += two_weeks
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if day >= 31:
            month += 1
            day -= 30
            if month > 12:
                year += 1
                month = 1
    else:
        if day >= 30:
            month += 1
            day -= 29
        
    print(f"{year}-{month}-{day}")