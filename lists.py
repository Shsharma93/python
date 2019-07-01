
# list
def lists_demo():
    numbers = [1, 2, 3, 4, 5, 6]
    fruits = ['Mango', 'Apple', 'Oranges', 'Banana']
    print(numbers)
    print(fruits[1])
    print(len(fruits))
    print(len(fruits[2]))
    fruits.append('Lichi')
    fruits.remove('Mango')
    fruits.insert(2, 'Grapes')
    fruits.pop(3)
    fruits.reverse()
    fruits.sort()
    fruits.sort(reverse=True)
    fruits[0] = 'Strawberries'
    print(fruits)


# lists_demo()


# Tuples - ordered and unchangeable
def tuple_demo():
    fruits = ('Mango', 'Apple', 'Grapes')
    fruits2 = ('Apple', 'Oranges', 'Lichi')
    print(fruits)
    # fruits[2] = 'Banana'
    del fruits2  # delete tuple
    print(fruits[1])


# tuple_demo()


# Sets - Unordered and unindexed. No Duplicate
def sets_demo():
    fruits_set = {'Apple', 'Oranges'}
    print('Apple' in fruits_set)
    fruits_set.add('Grapes')
    fruits_set.remove('Grapes')
    # fruits_set.clear()
    # del fruits_set
    print(fruits_set)


# sets_demo()


# Dictionary
def dictionary_demo():
    person = {
        'first_name': 'Shashank',
        'last_name': 'Kumar',
        'age': 25,
        'is_programmer': True
    }

    person['phone'] = '0451 288 706'

    print(person)
    print(person['first_name'])
    print(person.keys())
    print(person.items())

    person2 = person.copy()
    person2['city'] = 'Brisbane'
    del(person2['city'])
    person.pop('age')
    person.clear()
    print(person2)
    print(len(person2))

# list of dictionary
    people = [
        {'name': 'Shashank', 'age': 24},
        {'name': 'Shakya', 'age': 16}
    ]
    print(people[1])
    print(people[1]['name'])


# dictionary_demo()