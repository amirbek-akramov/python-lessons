"""
GitHub: https://github.com/amirbek-akramov/python-lessons
#34 - lesson: JSON
Date: 29/03/2023
"""
import json



# x = 10
# x_json = json.dumps(x)
# print(f"\nPython {x} type: {type(x)} \n Json {x_json} type: {type(x_json)}")

# y = 5.5
# y_json = json.dumps(y)
# print(f"\nPython {y} type: {type(y)} \n Json {y_json} type: {type(y_json)}")

# boolean = True
# bool_json = json.dumps(boolean)
# print(f"\nPython {boolean} type: {type(boolean)} \n Json {bool_json} type: {type(bool_json)}")

# none = None
# none_json = json.dumps(none)
# print(f"\nPython {none} type: {type(none)} \n Json {none_json} type: {type(none_json)}")

# lists = ["JSON", "JavaScript", "Python", "Golang"]
# lists_json = json.dumps(lists)
# print(f"\nPython {lists} type: {type(lists)} \n Json {lists_json} type: {type(lists_json)}")

# tpl = ("JSON", "JavaScript", "Python", "Golang")
# tpl_json = json.dumps(tpl)
# print(f"\nPython {tpl} type: {type(tpl)} \n Json {tpl_json} type: {type(tpl_json)}")

# dicts = {'apple': 0.50, 'banana': 0.25, 'orange': 0.75, 'grapes': 1.50}
# dict_json = json.dumps(dicts)
# print(f"\nPython {dicts} type: {type(dicts)} \n Json {dict_json} type: {type(dict_json)}")


"""
To transform js file (JSON) to python use "loads()"
"""

# lists = ["JSON", "JavaScript", "Python", "Golang"]
# lists_json = json.dumps(lists)
# print("Python list converted to JavaScript:", lists_json) # you can't work with this list because it is string
# lists_json = json.loads(lists_json)
# print("Converted back like Python list:", lists_json) # you can work with this list

my_dict = {
    'outer_list': [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Bob', 'age': 40},
        {
            'inner_dict': {
                'inner_list': [
                    {'name': 'Alice', 'age': 35},
                    {'name': 'David', 'age': 45},
                    {'name': 'Eve', 'age': 50}
                ]
            }
        }
    ]
}

my_dict_json = json.dumps(my_dict)
print("\n",my_dict_json, "\n",type(my_dict_json))

# conveted from json to python

my_dict2 = json.loads(my_dict_json)
print("\n", my_dict2, "\n",type(my_dict2))

# write json file

file_name = "JSON/json_file.json"

with open(file_name, "w") as file:
    json.dump(my_dict, file)

# next file named "next_json_file"
