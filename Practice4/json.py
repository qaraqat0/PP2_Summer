import json

student = {
    "name": "Kara",
    "age": 20,
    "university": "KBTU"
}

json_string = json.dumps(student, indent=4)

print(json_string)

data = json.loads(json_string)

print(data["name"])

with open("sample-data.json", "w") as file:
    json.dump(student, file, indent=4)

with open("sample-data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)