
def write_file():
    file = open('abc.txt', 'w')
    file.write('Shashank')


def read_file():
    file = open('abc.txt')
    text = file.read()
    print(text)


# write_file()
#read_file()