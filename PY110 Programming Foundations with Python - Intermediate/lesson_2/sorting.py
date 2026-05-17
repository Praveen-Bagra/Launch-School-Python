# lst = ['arc', 'bat', 'cape', 'ants', 'cap']
# print(sorted(lst))
# Prints ['ants', 'arc', 'bat', 'cap', 'cape']

# vowels = ['u', 'i', 'a', 'e', 'o']
# sorted_vowels = sorted(vowels)
# print(vowels)
# print(sorted_vowels)

# vowels = ['u', 'i', 'a', 'e', 'o']
# vowels.sort()
# print(vowels)

# print(ord('+'))
# print(ord('3'))
# print('+' < '3')

# print('A' < 'a')
# print('Z' < 'a')
# print('!' < 'A')

# numbers = [2, 11, 9, 4, 107, 21, 1]
# lst = sorted(numbers, reverse=True)
# print(lst)

# words = ['arc', 'bat', 'cape', 'ants', 'cap']
# lst = sorted(words, reverse=True)
# print(lst)

# tup = (8, 23, 4, 134, 2)
# sorted_tup = tuple(sorted(tup))

# print(sorted_tup)

# words = ['apple', 'pie', 'shortcake']
# sorted_words = sorted(words, key=len)
# print(sorted_words)

# def lowercase(str):
    # return str.lower()

# animals = ['Cat', 'dog', 'ZEBRA', 'monkey']
# sorted_animals = sorted(animals, key=str.lower)
# print(sorted_animals)

def person_key(person):
    name, age = person
    return (age, name)

people = [('Jack', 30), ('John', 25), ('Betty', 25), ('Anna', 30)]
sorted_people = sorted(people, key=person_key)
print(sorted_people)