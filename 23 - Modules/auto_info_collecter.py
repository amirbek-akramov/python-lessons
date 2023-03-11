def auto_info(company, model, color, auto_type, year,costs=None):
    car = {
        "company":company,
        "model":model,
        "color":color,
        "type":auto_type,
        "year":year,
        "cost":costs
    }
    return car

def add_auto():
    cars = []
    while True:
        company = input("Company: ")
        model = input("Model: ")
        color = input("Color: ")
        auto_type = input("Type: ")
        year = int(input("Year: "))
        costs = int(input("Cost: "))
        
        cars.append(auto_info(company.lower(), model.lower(), color.lower(), auto_type.lower(), year, costs))
        
        answer = input("Do you want to add more (yes/no): ")
        if answer != 'yes':
            break
        
        
def auto_print(auto_info):
    print(f"{auto_info['color'].title()} {auto_info['company'].upper()}"
          f"{auto_info['model'].upper()}, Auto type: {auto_info['auto_type']}."
          f"{auto_info['year']} - year, {auto_info['costs']}"
          )
    