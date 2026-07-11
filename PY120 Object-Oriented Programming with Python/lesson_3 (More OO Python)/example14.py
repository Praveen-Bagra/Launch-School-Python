# class Animal:
    # def __init__(self, name):
        # self.name = name

# class Dog(Animal):
    # def speak(self):
        # return f'bark! bark! {self.name} bark! bark!'

# teddy = Dog('Teddy')
# print(teddy.speak())

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'bark! bark! {self.name} bark! bark!'

teddy = Dog('Teddy')
print(teddy.speak())
print(teddy.get_name())