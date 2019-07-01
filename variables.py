# variables & string
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
    # full = first + " " + last
    full = f"{first} {len(last)} {2+4}"

    print(first.replace("s", "S"))
    print('s' in first)
    print('swift' not in first)
    print(full)
    print(first.split(" "))


variables_demo()
