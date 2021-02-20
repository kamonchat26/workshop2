import json

# some JSON
json_string = '{ "name": "Pin & kamon", "age":21,"city": "Bangkok"}'

python_dict = json.load(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])