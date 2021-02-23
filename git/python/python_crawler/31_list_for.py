pets = [
    {"name": "nabi", "age": 4, "kind": "cat"},
    {"name": "mary", "age": 5, "kind": "dog"},
    {"name": "dragon", "age" : 1, "kind" : "lizard"}
]

print(len(pets))

for pet in pets:
    print(pet['age']*1000)
    print(pet['kind'], pet['name'])