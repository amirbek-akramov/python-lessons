import pickle

"Practise"

my_info = "31122009"

with open("pi_million_digits/pi_million_digits.txt", "r") as file:
    pi = file.read()

pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = pi.replace(" ", "")


if my_info in pi:
    print("I found it")
else:
    print("I can't found") 

pi = float(pi)

"""""_#_#_#_#_#_#_#_#_#_#______________________#_#_#_#_#_#_#_#_"""""

file_python = "practise_test_python_file/practise_test_python_file.py"

with open(file_python, "wb") as file:
    pickle.dump(pi, file)

with open(file_python, "rb") as file:
    pickles = pickle.load(file)

print(pickles)