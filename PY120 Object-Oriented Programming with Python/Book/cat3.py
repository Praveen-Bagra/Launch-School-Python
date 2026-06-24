class Cat:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
            
        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name

class Dog:

    def __init__(self, first_name):
        self.first_name = first_name

fluffy = Cat('Fluffy')
tommy = Dog('Tommy')
print(fluffy == tommy)
