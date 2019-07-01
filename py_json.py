import json

userJSON = '{"first_name": "Shashank", "last_name": "Kumar", "age": "25"}'

user = json.loads(userJSON)

print(user)


for person, info in user.items():
    print(person, info)


car = {
    'make': 'Toyota',
    'model': 'Camry',
    'year': 2018
}


carJSON = json.dumps(car)

print(carJSON)