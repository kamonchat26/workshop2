dict1 = {"name": "pipusna", "age": "26"}
dict2 = {"name": "pipusna", "age": "26"}
dict3 = dict1

print(dict1 is dict3)  # output : True

print(dict1 is dict2)  # output : False

print(dict1 == dict2)  # output : True
