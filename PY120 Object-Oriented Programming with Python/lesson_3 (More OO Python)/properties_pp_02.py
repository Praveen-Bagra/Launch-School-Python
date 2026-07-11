class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string and shouldn't be empty.")

        if name == "":
            raise ValueError("Name must not be empty.")

        self._name = name

praveen = Person("Praveen")
print(praveen.name)

praveen.name = "Praveen Bagra"
print(praveen.name)

# mohan = Person(777)
# print(mohan.name)

mohan = Person("")
print(mohan.name)

