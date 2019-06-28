

#variables & string
def variables_demo():
    print("hello world")
    print("*" * 10)
    age = 26  # int
    ratings = 4.9  # float
    isPublished = True  # boolean
    print(age)
    print(isPublished)
    print(ratings)
    course = "Python Programming"  # stirng

    x, y, is_cool, name = (3, 4.5, False, 'James')  # multiple assignment

    x = str(x)
    y = int(y)

    print(type(x), is_cool, name)

    message = """
  Hi, How are you?
  I'm fine.
  """
    len(course)
    print(course[0])  # first letter of string
    print(course[-1])  # last leeter of string
    print(course[2:5])  # 2-5 chars of string
    print(message)

    first = 'shashank'
    last = 'Kumar'
    print(first.upper())
    print(first.title())
    print(last.lower())
    print(first.capitalize())
    print(first.swapcase())
    # remove white space form start and end of string rstrip() lstrip()
    print(first.strip())
    print(last.find('ma'))  # index
    #full = first + " " + last
    full = f"{first} {len(last)} {2+4}"

    print(first.replace("s", "S"))
    print('s' in first)
    print('swift' not in first)
    print(full)
    print(first.split(" "))


# variables_demo()


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
    #del fruits_set
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


def sayHello(name="Shashank"):
    print('Hello ' + name)
    print(f'Hello {name}')


# sayHello()


def getSum(a, b):
    return a+b


#sum = getSum(5, 6)


# if else elif


def conditionals_demo(x, y, z):
    if x > y and x > z:
        print(f'{x} is greater than {y} and {z}')
    elif y > x and y > z:
        print(f'{y} is greater than {x} and {z}')
    elif z > x and z > y:
        print(f'{z} is greater than {x} and {y}')
    elif x == y and x != z:
        if x > z:
            print(f'{x} and {y} are equal and greater than {z}')
        elif x < z:
            print(f'{x} and {y} are equal but less than {z}')
    elif x == z and z != y:
        if x > y:
            print(f'{x} and {z} are equal and greater than {y}')
        elif y < x:
            print(f'{x} and {z} are equal but less than {y}')
    elif y == z and y != x:
        if y > x:
            print(f'{y} and {z} are equal and greater than {x}')
        elif y < x:
            print(f'{y} and {z} are equal but less than {x}')
    else:
        print(f'{x}, {y} and {z} are equal')


#conditionals_demo(30, 30, 60)

def in_not_in(x, y, numbers):
    if x in numbers:
        print(f'{x} in the list.')
    if y not in numbers:
        print(f'{y} not in the list.')


#in_not_in(3, 4, [1, 2, 3])


def is_not(x, y):
    if x is y:
        print(f'{x} is {y}')
    if x is not y:
        print(f'{x} is not {y}')


is_not(4, 4)
