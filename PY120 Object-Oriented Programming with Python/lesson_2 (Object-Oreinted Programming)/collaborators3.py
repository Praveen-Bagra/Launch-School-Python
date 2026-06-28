class Person:

    def __init__(self, name):
        self.name = name
    
class Dog:

    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fething!'

class BullDog(Dog):
    pass

bob = Person('Robert')
bud = BullDog()

bob.pet = bud
print(bob.pet)
print(bob.pet.speak())
print(bob.pet.fetch())