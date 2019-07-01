
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


# conditionals_demo(30, 30, 60)

def in_not_in(x, y, numbers):
    if x in numbers:
        print(f'{x} in the list.')
    if y not in numbers:
        print(f'{y} not in the list.')


# in_not_in(3, 4, [1, 2, 3])


def is_not(x, y):
    if x is y:
        print(f'{x} is {y}')
    if x is not y:
        print(f'{x} is not {y}')


# is_not(4, 4)



