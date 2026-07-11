class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed


dog1 = Dog("Golden Retriever")
print(dog1.get_breed())
dog1._breed = 'Labrador'
print(dog1.get_breed())
