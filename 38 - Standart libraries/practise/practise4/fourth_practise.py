"Practise 4"

import re

telephone_number = input("Telephone number: ")

def check_tn(telephone_number):
    andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    
    telephone_number = telephone_number.replace(" ", "")
    
    checking = re.match(andoza, telephone_number)
    
    if checking:
        print("Thank you!")
    else:
        print("Write normal telephone number")
        
check_tn(telephone_number)