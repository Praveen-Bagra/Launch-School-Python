# def welcome(name):
    # print(f"Welcome, {name}!")

# print(welcome)
# welcome('Victor')

# class Greeter:
    # def __init__(self, name):
        # self.name = name

# greet_instance = Greeter('Srdjan')
# print(Greeter)

class Individual:
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
        print(f'I am called {self.name}')
        
person = Individual('Bob')
person()