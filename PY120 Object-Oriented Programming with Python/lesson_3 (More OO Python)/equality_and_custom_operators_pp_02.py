class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()
        
        
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() != other.name.casefold()
        
class Dog:
    def __init__(self, name):
        self.name = name

kitty = Cat('Fido')
kitty2 = Cat('fiDo')
kitty3 = Cat('Fido')
kitty4 = Cat('Sona')
tommy = Dog('Captain')



print(kitty == kitty2) # True
print(kitty == kitty3 ) # True
print(kitty == kitty4) # False
print(kitty == tommy) # False

print()

print(kitty != kitty2) # False
print(kitty != kitty3 ) # False
print(kitty != kitty4) # True
print(kitty != tommy) # True

print()

print(kitty == 'bugs')
print(kitty != 'bugs')