class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age == other.age

    def __ne__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age != other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age < other.age

    def __le__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age <= other.age

    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age > other.age

    def __ge__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age >= other.age
    
ted = Person('Ted', 33)
carol = Person('Carol', 49)

if ted < carol:
    print('Ted is younger then Carol')
else:
    print('Ted is older then Carol')

# print(1 + 2)
# print(1 + 2 == 3)

# print((1).__add__(2))
# print((1).__add__(2).__eq__(3))