import json

data = {"name": "jk", "age": 25,"country":"seoul"}

with open("tym.json", "w") as file:
    json.dump(data, file, indent=4)

assert data["name"] == "jk"
assert data["age"] == 25
assert data["country"] == "seoul"