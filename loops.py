def loops(people):
    for person in people:
        if person is 'Shivani':
            break  # continue
        print(person)
    for i in range(-1, 20, 2):  # range(5) , range(5, 10)
        print(i)
    for x in "Python":
        print(x)


def loops_demo():
    name = "Shashank"

    for character in name:
        print(character)


# loops_demo()


def while_demo():
    user_entered = True

    while user_entered is True:
        print(10)
        user_input = input('Should we print again ? (y/n) :  ')

        if user_input is 'n' or 'N':
            user_entered = False


# while_demo()

def for_else_demo():
    successful = False
    for number in range(3):
        print('Attempt')
        if successful:
            print("Successful")
            break
    else:
        print("Attempted 3 times and failed.")


#for_else_demo()

loops(['Shashank', 'Shivani', 'Shakya', 'Shipra'])
