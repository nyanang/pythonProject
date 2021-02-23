#pet list 애완동물 강아지, 고양이, 도마뱀

pets = [{"name": "nabi", "age": 4, "kind": "cat"},
        {"name": "mary", "age": 5 ,"kind": "dog"},
        ]
pet3 = {"name": "dragon", "age" : 1, "kind" : "lizard"}
pets.append(pet3)
print(pets)
print(len(pets))

pet1 = pets[0]
print("pet1:", pet1)
print(pet1['kind'])
print(pets['kind'])