class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

# _cats_count is a class variable. It is counting the instances of 
# the Cat class created. 

cat1 = Cat("Don't know")
print(Cat.cats_count())

cat2 = Cat("Don't know")
print(Cat.cats_count())

cat3 = Cat("Don't know")
print(Cat.cats_count())