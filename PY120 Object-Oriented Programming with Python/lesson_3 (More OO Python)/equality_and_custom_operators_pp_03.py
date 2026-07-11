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

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() <= other.name.casefold()
        
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()

kitty = Cat('Fido')
kitty2 = Cat('fido')
sona = Cat('Sona')

print(kitty > kitty2)
print(kitty >= kitty2)
print(kitty > sona)
# print(kitty > 'Fido')
print()
print(kitty < kitty2)
print(kitty <= kitty2)
print(kitty < sona)
# print(kitty < 'Fido')
