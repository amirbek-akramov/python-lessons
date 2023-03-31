import json

"Practise"

""" # 1 """

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

# data_json = json.dumps(data)

# print(data_json)
# print(type(data_json))


""" # 2 """

# talaba = {"ism":"Hasan","familiya":"Husanov","tyil":2000}

# with open("JSON/practise_json.json", "w") as json_file:
#     json.dump(talaba, json_file)

# with open("JSON/practise_json.json", "r") as file:
#     talaba = json.load(file)

# print(talaba["ism"])
# print(talaba["familiya"])

""" # 3 """

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}


# talaba = {"ism":"Hasan","familiya":"Husanov","tyil":2000}


# with open("JSON/practise_json_main_1.json", "w") as data_file:
#     json.dump(data, data_file)

# with open("JSON/practise_json_main_2.json", "w") as talaba_file:
#     json.dump(talaba, talaba_file)


""" # 4 """

# with open("JSON/students.json") as students_json:
#     data = json.load(students_json)

# for item in data["student"]:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")



""" # 5 """

with open("JSON/api-result.json") as api_json_file:
    wiki_api = json.load(api_json_file)

print(wiki_api["query"]["pages"]["13801"]["title"])
print(wiki_api["query"]["pages"]["13801"]["extract"])