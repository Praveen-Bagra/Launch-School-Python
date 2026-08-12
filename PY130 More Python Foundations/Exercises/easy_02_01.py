def greet(name, greeting, punctuation_mark='.'):
    return f'{greeting}, {name}{punctuation_mark}'

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good morning, Pete!