class Cat:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Cat({repr(self.name)})'

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

fuzzy = Cat('Fuzzy')
fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')

print(fuzzy == fluffy)
print(fluffy == fluffy)
print(fuzzy != fluffy)
print(fuzzy != fuzzy)

print(fluffy == fluffy2)
print(fluffy != fluffy2)

print(fluffy.__eq__(fluffy2))