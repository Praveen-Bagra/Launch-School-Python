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

fluffy = Cat('Fluffy')
whiskers = Cat('Whiskers')

print(fluffy == whiskers)
print(fluffy != whiskers)

print(fluffy < whiskers)