class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self._age = age
        self.__breed = breed

    def __str__(self):
        return f'''
My name is {self.name}.
I am {self._age} years old.
I am a {self.__breed}.
'''

rover = Dog('Rover', 4, 'Mutt')
print(rover)

rover.name = 'Fido'
rover._age = 7
rover.__breed = 'Poddle'
print(rover)

print(rover.__breed)
print(rover._Dog__breed)

rover._Dog__breed = 'Boxer'
print(rover)