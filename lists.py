
# list


def lists_demo():
    numbers = [1, 2, 3, 4, 5, 6]
    fruits = ['Mango', 'Apple', 'Oranges', 'Banana']
    first, second, *others = numbers  # list unpacking first, *others, last
    print(first, second, others)
    print(sorted(fruits))
    first,  *others, last = numbers
    print(numbers.count(5))  # print number of times 5 in the lists
    print(first, last, others)
    print(fruits[-1])  # Banana
    print(numbers[0:3:2])  # 1,3
    print(numbers[::-1])  # 6,5,4,3,2,1
    print(numbers * 5)
    print(numbers + fruits)
    print(list(range(1, 20, 3)))
    print(list("Shashank"))
    print(numbers)
    print(fruits[1])
    print(len(fruits))
    print(len(fruits[2]))
    fruits.append('Lichi')  # at the end
    fruits.remove('Mango')
    fruits.insert(2, 'Grapes')  # insert at specific position
    del fruits[0:2]  # remove elements from index 0 to 2
    fruits.pop(3)  # remove specific element
    fruits.pop()  # remove last element
    fruits.reverse()
    fruits.sort()
    fruits.sort(reverse=True)
    fruits[0] = 'Strawberries'
    print(fruits)


# lists_demo()


def lists_loop(letters):
    for index, letter in enumerate(letters):
        print(index, letter)

    if 'e' in letters:
        print(letters.index('e'))


lists_loop(['a', 'b', 'c', 'd', 'e'])

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


def set_operations(operation_type):
    number_1 = {1, 4, 6, 8, 12}
    number_2 = {3, 6, 1, 5}

    if operation_type is 'union':
        return number_1.union(number_2)
    elif operation_type is 'intersection':
        return number_1.intersection(number_2)
    elif operation_type is 'diff':
        return number_2.difference(number_1)


# print(set_operations('diff'))

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
