# nums = [1, 2, 2, 3, 3, 3]
# print(nums.count(3))
# print(nums.count(0))

# fruits = ['apple', 'orange', 'banana', 'apple', 'grape']
# print(fruits.index('apple'))
# print(fruits.index('apple', 1))
# print(fruits.index('apple', 1, 3))

# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)

# numbers.insert(2, 'two-point-five')
# print(numbers)

# numbers = [1, 2, 3]
# numbers.insert(3, 4)
# numbers.insert(1000, 5)
# print(numbers)

# numbers = [1, 2, 3]
# numbers.extend([4, 5, 6, 7])
# print(numbers)

# numbers.extend({8, 9, 10})
# print(numbers)

# numbers = [1, 2, 'two-point-five', 3, 4]
# numbers.remove('two-point-five')
# print(numbers.pop(2))
# print(numbers)
# print(numbers.pop())
# print(numbers)

# numbers.remove(10)

# lst = []
# lst.pop()

# numbers = list(range(1, 7))
# numbers.reverse()
# print(numbers)

# numbers = [61, 103, 525, 10100, 25, 3]
# numbers.sort()
# print(numbers)

# numbers = ['61', '103', '525', '10100', '25', '3']
# numbers.sort()
# print(numbers)

# animals = ['cat', 'aardvark', 'horse', 'python', 'orangutan']
# animals.sort()
# print(animals)

# numbers = ['61', '103', 525, '10100', '25', '3']
# numbers.sort()

# animals = ['cat', 'aardvark', 'horse', 'python', 'orangutan']
# animals.sort(reverse=True)
# print(animals)

# animals = ['Cat', 'aarDVARK', 'HORSE', 'Python', 'orangutan']
# animals.sort()
# print(animals)

# animals.sort(key=str.casefold)
# print(animals)

# numbers = ['61', '103', '525', '10100', '25', '3']
# numbers.sort(key=int)
# print(numbers)

# numbers = ['61', '103', 525, '10100', '25', '3']
# numbers.sort(key=str)
# print(numbers)

# shades = ('crimsion', 'emerald', 'azure')
# r, g, b = shades
# print(r)
# print(g)
# print(b)

# nums = (1, 2, 2, 3, 3, 3)
# print(nums.count(3))
# print(nums.count(4))

# fruits = ('apple', 'orange', 'banana', 'apple', 'grape')
# print(fruits.index('apple'))
# print(fruits.index('apple', 1))
# print(fruits.index('apple', 1, 3))

# print(list('apple'))
# print(tuple('banana'))

# fruits_list = ['apple', 'banana', 'cherry']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)

# print(list(fruits_tuple))

# book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965}
# key_view = book.keys()
# print(key_view)

# book['publisher'] = 'Chilton Books'
# print(key_view)

# book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965}
# key_list = list(book.keys())
# print(key_list)

# book['genre'] = 'Science Fiction'
# print(key_list)

# print(list(book.keys()))

# data = {'apple': 5, 'banana': 3, 'cherry': 8}
# print(list(data.keys()))

# print(tuple(data.keys()))

# data = {'apple': 5, 'banana': 3, 'cherry': 8}
# print(list(data.values()))

# print(tuple(data.values()))

# data = {'apple': 5, 'banana': 3, 'cherry': 8}
# print(list(data.items()))

# print(tuple(data.items()))

# fruits_set = {'apple', 'banana', 'cherry'}
# print(list(fruits_set))
# print(tuple(fruits_set))

# fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
# print(list(fruits_frozenset))

# print(tuple(fruits_frozenset))

# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
    # print(fruit)

# colors = ('red', 'green', 'blue')
# for color in colors:
    # print(color)

# fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
    # print(f'Index {index} has fruit: {fruit}')

# colors = ('red', 'green', 'blue')
# for index, color in enumerate(colors):
    # print(f'Color at index {index} is {color}')