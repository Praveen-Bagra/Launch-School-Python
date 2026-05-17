# print(list(range(3)))
# print(list(range(1, 3)))
# print(list(range(1, 6, 2)))
# print(list(range(6, 1, -1)))

# for i in range(5):
    # print(i)

# colors = ['red', 'green', 'blue']
# for idx, color in enumerate(colors):
    # print(f"Color {color} is at index {idx}.")

# my_range = range(10)
# print(my_range.count(5))
# print(my_range.count(15))
# print(my_range.index(5))

# print(my_range.index(15))
# print(my_range.start)
# print(my_range.stop)
# print(my_range.start)

# sentence = 'Hello, world!'
# position = sentence.index('world')
# print(position)

# print(sentence.index('school'))

# sentence = 'Hello, world!'
# position = sentence.find('world')
# print(position)

# position = sentence.find('school')
# print(position)

# my_str = 'Monty Python writes Pythonic Python'
# print(my_str.count('Python'))
# print(my_str.count('y'))
# print(my_str.count('zip'))

# sentence = 'Hello World'
# position = sentence.index('l', 6)
# print(position)

# position = sentence.find('l', 6)
# print(position)

# my_str = 'Monty Python writes Pythonic Python'
# print(my_str.count('Python', 10))

# sentence = 'Hello World'
# position = sentence.index('l', 3, 7)
# print(position)

# position = sentence.index('d', 3, 7)
# print(position)

# position = sentence.find('l', 3, 7)
# print(position)

# position = sentence.find('d', 3, 7)
# print(position)

# my_str = 'Monty Python writes Pythonic Python'
# print(my_str.count('Python', 10, 26))

# my_str = 'aab'
# print(my_str.count('a', 0, 1))

# price = '$45,000'
# cleaned_price = price.replace('$', '')
# print(cleaned_price)

# string = "This is the first line.\nThis is still the first line.\nThis is the second line."
# cleaned_string = string.replace('\n', '', 1)
# print(cleaned_string)

# print('pete'.upper())
# print('PETE'.lower())

# print('straße'.lower())
# print('straße'.casefold())

# print('pete'.capitalize())
# print('PeTe'.swapcase())

# print('Straße'.swapcase())
# print('Straße'.swapcase().swapcase())

# connector = '--'
# fruits = ['apple', 'berry', 'citrus']
# print(connector.join(fruits))

# print(''.join(['a', 'b', 'c', 'd']))

# numbers = [1, 2, 3, 4, 5]
# print('-'.join([str(num) for num in numbers]))

# data_line = 'apple,berry,citrus'
# print(data_line.split(','))

# data_line = 'apple   berry  citrus'
# print(data_line.split())
# print(data_line.split(' '))

# data_line = 'apple-berry-citrus-dragonfruit'
# print(data_line.split('-', 2))
# print('apple'.split(''))

# print(list('apple'))
# print(tuple('apple'))

# print(repr('   abcdef  '.strip()))
# print(repr('   abcdef  '.lstrip()))
# print(repr('   abcdef  '.rstrip()))

# print('aaabcdefaa'.strip('a'))

# print('hello'.startswith('he'))
# print('hello'.endswith('lo'))

# print('abc'.isalpha())
# print('abc123'.isalnum())
# print('123'.isdigit())
# print('  '.isspace())

# print(''.isalpha())
# print('straße'.isalpha())

# print(repr(str([1, 2, 3])))
# print(repr(str(123)))

# print(repr(str(1.2)))
# print(repr(str(True)))
# print(repr(str(None)))

# print(repr(str([1, 2, 3])))
# print(repr(str((1, 2, 3))))

# print(repr(str({1, 2, 3})))

# print(repr(str(frozenset([1, 2, 3]))))

# print(repr(str({'foo': 41, 'bar': 'xyz'})))

# for char in 'hello':
    # print(char)

# word = 'hello'
# index = 0
# while index < len(word):
    # print(word[index])
    # index += 1