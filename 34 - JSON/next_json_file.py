import json

# convert from json file


with open("JSON/json_file.json") as json_file:
    my_dict = json.load(json_file)

# print(my_dict, "\n", type(my_dict))

# working with dicts

name = my_dict["outer_list"][3]["inner_dict"]["inner_list"][1]["name"]
age = my_dict["outer_list"][3]["inner_dict"]["inner_list"][1]["age"]

print(f"Json converted dict info finding: \n Name: {name} \n Age: {age}")