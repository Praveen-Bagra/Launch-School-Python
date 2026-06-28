class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()

# ['Cat', 'Animal', 'object']
print(Cat.mro())