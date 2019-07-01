

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greetings(self):
        return f'I am {self.name}. My age is {self.age}.'

    def birth_year(self):
        return 2019 - self.age


class Customer(User):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def greetings(self):
        return f'I am {self.name}. My age is {self.age}. My balance is {self.balance}'


shashank = User('Shashank', 'shsharma93@gmail.com', 25)
virat = Customer('virat', 28)

print(shashank.name)
print(shashank.greetings())
print(shashank.birth_year())
virat.set_balance(200)
print(virat.get_balance())
print(virat.greetings())
