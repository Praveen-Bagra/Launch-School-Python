class Animal:
    total_animals = 0

    def __init__(self):
        self.__class__.total_animals += 1

class Dog(Animal):
    def animal_count(self):
        return self.__class__.total_animals

spike = Dog()
print(spike.total_animals)
print(spike.animal_count())