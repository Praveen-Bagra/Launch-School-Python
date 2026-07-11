class Person:
    name = 'leslie'.capitalize() * 3 + '!'
    letters = [letter for letter in 'leslie']

print(Person.name)
print(Person.letters)