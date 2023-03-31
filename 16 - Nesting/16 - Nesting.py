"""
GitHub: https://github.com/amirbek-akramov/python-lessons
# 16-dars: Nesting
sana: 25/02/2023
"""

# car_0 = {
#     "model":"nexia 3",
#     "color":"black",
#     "year":2001,
#     "cost":7_000,
#     "km":30_000,
#     "type":"auto"
# }

# car_1 = {
#     "model":"lacetti",
#     "color":"red",
#     "year":2004,
#     "cost":7.5_000,
#     "km":60_000,
#     "type":"mannual"
# }

# car_2 = {
#     "model":"gentra",
#     "color":"cornflowerblue",
#     "year":2006,
#     "cost":11_000,
#     "km":70_000,
#     "type":"auto"
# }

# car_3 = {
#     "model":"tico",
#     "color":"brown",
#     "year":1994,
#     "cost":2_000,
#     "km":10_000, 
#     "type":"mannual"
# }

# car = car_0
# car = car_1
# car = car_2
# car = car_3
# print(f"{car['model'].title()}-model, "
#       f"{car['color'].title()}-color, "
#       f"{car['year']}-year, {car['cost']}$")



# cars = [car_0, car_1, car_2, car_3]

# for car in cars:
#     print(f"{car['model'].title()}-model, "
#     f"{car['color'].title()}-color, "
#     f"{car['year']}-year, {car['cost']}$")

# print(cars[0])
# print(cars[0]['model'])

# print(cars[2]['model'], cars[2]['color'].title())



# cars = []

# for n in range(10):
#     new_car = {
#         "model":"Tracker",
#         "color":None,
#         "year":1994 + n//3,
#         "cost":2_000 + n*100.2,
#         "km":0000,
#         "type":"mannual"
#     }
#     cars.append(new_car)
    
# for car in cars:
#     print(car)
    
# __#__#__#__#__#__#

# for car in cars:
#     print(car['cost'])
    
#__#__#__#__#__#__#
    
# for car in cars[:3]:
#     car['color'] = 'red'
    
    
# for car in cars:
#     print(car)
    
#__#__#__#__#__#__#

# for car in cars[3:6]:
#     car['color'] = 'black'

# for car in cars:
#     print(car)
    
#__#__#__#__#__#__#

# for car in cars[6:]:
#     car['color'] = 'brown'
#     car['type'] = 'auto'
    
# for car in cars:
#     print(car)
    


#__#__#__#__#__#__#__#__#__#__#__#


# for car in cars:
#     if car['type']=='auto':
#         car['cost']=40000
#     else:
#         car['cost']=35000
        
# for car in cars:
#     print(f"Car is {car['type']} and it costs {car['cost']}$")
    
    
    
    
    
# programmers = {
#     "temurbek":['c++', "java", "kotlin"],
#     "amirbek":["html","css","javascript","python","sqlite","django","golang"],
#     "arbarshoh":["c#","c"],
#     "a'zamshoh":["c"],
# }

# for programmer, programms in programmers.items():
#     print(f"\n{programmer.title()} manashu tillarda code yozadi:")
#     for programm in programms:
#         # print(programm.upper())
#         print(programm.upper(), end = ' / ')


"""
"Dictionaries" into "Dictionaries"

_______________________________________________________________________________
"""

# professors = {
#     'ali':{'surname':'valiyev',
#            'birth_year':1995,
#            'info':'special',
#            'languages':['python','c++']
#            },
#     'vali':{'surname':'aliyev',
#             'birth_year':2001,
#             'info':"medium-special",
#             'languages':['html', 'css', 'js']},
#     'hasan':{'surname':'husanov',
#              'birth_year':1999,
#              'info':'special',
#              'languages':['python','php']}
# }

# for name, info in professors.items():
#     print(f"\n{name.title()} {info['surname'].title()}, "
#           f"{info['birth_year']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['info']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for language in info['languages']:
#         print(language.upper())



"""
Practice 1

_______________________________________________________________________________
"""

# writers = {
#     "abu abdulloh muhammad ibn ismoil":{'birth_year':810, 'where':"Bukhara", 'live':60},
#     "abdulla qodiriy":{'birth_year':1894, 'where':"tashkent", 'live':44},
#     "erkin vohidov":{'birth_year':1936, 'where':"ferghana", 'live':80},
#     "alisher navai":{'birth_year':1441, 'where':"khirot", 'live':60}
# }

# for writer, info in writers.items():
#     print(writer.title(),end='')
#     print(f" was born in {info['birth_year']} in {info['where'].title()}. He was lived {info['live']} years\n")
        


"""
Practice 2

_______________________________________________________________________________
"""


# writers = {
#     "abu abdulloh muhammad ibn ismoil":["al-jome'", "as-sahih","al-adab","al-mufrad","at-tarix","al-kabir"],
#     "abdulla qodiriy":["o'tkan kunlar","mehrobdan chayon","obid ketmon",],
#     "erkin vohidov":["tong nafasi","qo'shiqlarim sizga","o'zbegim","qiziquvchan matbusa"],
#     "alisher navai":["xamsa","lison ut-tayr","mahbub al-qulub","munojot",]
# }

# for writer, works in writers.items():
#     print(f"{writer.title()}'s famous works:", end='')
#     for work in works:
#         print(work.title())
#     print('\n')



"""
Practice 3

_______________________________________________________________________________
"""

# l_films = {
#     "ali":['titanic','terminator','matrix'],
#     "vali":['rambo','tenet','inception'],
#     "hoshim":['bomb','johm weak']
# }

# for name, films in l_films.items():
#     print(f"\n{name.title()}'s lovely film is ")
#     for film in films:
#         print(film.title())



"""
Practice 4

_______________________________________________________________________________
"""



# all_countries = {
#     "uzbekistan":{"capital":"tashkent" ,"area":"448978 km2", "population":33_000_000, "currency":"sum"},
#     "u.s.a":{"capital":"washington" ,"area":"963141418 km2", "population":327_000_000, "currency":"dollar"},
#     "malazia":{"capital":"kuala-lumpur" ,"area":"329750 km2", "population":25_000_000, "currency":"rinngit"}
# }


# for name, infos in all_countries.items():
#     print(f"\nThe capital of {name.title()} is {infos['capital']}: ")
#     for key, value in infos.items():
#         print(f"{key.title()}: {value}")



"""
Practice 5

_______________________________________________________________________________
"""

# choose = input("Search country: ")

# all_countries = {
#     "uzbekistan":{
#         "capital":"tashkent" ,
#         "area":"448978", 
#         "population":33_000_000, 
#         "currency":"sum"
#         },
    
#     "u.s.a":{
#         "capital":"washington",
#         "area":"963141418", 
#         "population":327_000_000, 
#         "currency":"dollar"
#         },
    
#     "malazia":{
#         "capital":"kuala-lumpur",
#         "area":"329750", 
#         "population":25_000_000, 
#         "currency":"rinngit"
#         }
# }


# if choose.lower() in all_countries:
    
#     info = all_countries[choose]
    
#     print(f"{choose.title()}'s capital is {info['capital'].title()}: ",
#           f"\nArea: {info['area']}, kv2",
#           f"\nPopulation: {info['population']},",
#           f"\nCurrency: {info['currency']}"
#           )
# else:
#     print("We can't find any information about this country")