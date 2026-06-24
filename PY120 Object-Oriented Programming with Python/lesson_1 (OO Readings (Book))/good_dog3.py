class GoodDog:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def speak(self):
        return f'{self.__name} says Arf!'

sparky = GoodDog('Sparky', 5)

sparky.__name = 'Fido'
print(sparky.__name)
print(sparky.speak())

sparky._GoodDog__name = 'Fido'
print(sparky._GoodDog__name)
print(sparky.speak())
