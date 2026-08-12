def say_pets(name, **pets):
    print(f"{name} pets are...:")
    for name, animal in pets.items():
        print(f'{name}, a lovely {animal}.')

say_pets('Pete', Cocoa='cat', Cheddar='cat')