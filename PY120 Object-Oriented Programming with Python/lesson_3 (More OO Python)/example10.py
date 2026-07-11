class Person:
    name = 'John'

    def get_name(self):
        return self.name

alice = Person()
sue = Person()
alice.name = 'Alice'
sue.name = 'Sue'

print(alice.get_name())
print(sue.get_name())
print(Person.name)