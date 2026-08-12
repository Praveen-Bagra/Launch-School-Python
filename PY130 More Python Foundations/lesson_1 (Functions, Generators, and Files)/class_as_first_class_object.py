class Cat:
    pass

class Dog:
    pass

def make_pet(pet_type, owner):
    pet = pet_type()
    pet.owner = owner
    return pet

cocoa = make_pet(Cat, 'Pete')
bobo = make_pet(Dog, 'Bruce')

print(type(cocoa))
print(type(Cat))