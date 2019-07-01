
def who_do_you_know():
    people = input('Enter the name of people you know, seperated by comma: ')
    people_list = people.split(',')
    return [person.strip() for person in people_list]


def ask_user():
    person = input('Enter the name: ')

    if person in who_do_you_know():
        print(f'User know {person}')
    else:
        print(f'User do not know {person}')


# ask_user()


def list_comprehension(num):
    print([x * 5 for x in range(num)])
    print([x for x in range(10) if x % 2 == 0])


# list_comprehension(6)

def multiple_args(*args, **kwargs):
    print(args)
    print(kwargs)


multiple_args(3, 4, 5, 6, 7, 8, 7, name="Shashank", location="Brisbane")
