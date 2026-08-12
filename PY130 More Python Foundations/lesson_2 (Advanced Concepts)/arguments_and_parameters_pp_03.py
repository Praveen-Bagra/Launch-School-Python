def describe_pet(animal_type, *, name=''):
    if name:
        print(f'{name} is a {animal_type}.')
    else:
        print(f"It's a {animal_type}. It don't have a name." )

describe_pet('cat', name='Fido')
describe_pet('dog')