class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.name == other.name

sue = Person('Sue')
jo = Person('Jo')

print(sue == jo)