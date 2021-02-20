import json


python_dict = {"name": "Pin & kamon", "age": 21, "city": "Bangkok"}

json_string = json.dumps(python_dict)

print(json_string)