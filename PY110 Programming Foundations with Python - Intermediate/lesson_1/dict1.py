# dict1 = {
    # 'fruit': 'apple',
    # 'vegetable': 'carrot',
    # 42: [1, 2, 3],
# }

# print(dict1['fruit'][3])

# print(dict1['vegetable'])

# print(dict1[42])

# dict2 = {
    # (1, 2, 3): 'hockey',
    # [4, 5, 6]: 'basketball',
# }

# dict1 = {
    # 'apple': 'fruit',
    # 'carrot': 'vegetable',
    # 'pear': 'fruit',
# }

# key = 'peach'
# print(dict1[key])

# key = 'banana'
# print(dict1.get(key))

# print(dict1.get('banana', 'not found'))

# print('apple' in dict1)

# print('banana' in dict1)

# print('banana' not in dict1)

# dict1 = {
    # 'apple': 'Produce',
    # 'carrot': 'Produce',
    # 'pear': 'Produce',
    # 'broccoli': 'Produce',
# }

# print(dict1)
# dict1['apple'] = 'Fruit'
# dict1['carrot'] = 'Vegetable'
# print(dict1)

# dict1['pear'] = 'Fruit'
# dict1['broccoli'] = 'Vegetable'
# print(dict1)

# dict1['watermelon'] = 'Fruit'
# print(dict1)

# del dict1['apple']
# print(dict1)

# fruits = {'apple', 'banana', 'cherry'}
# print('apple' in fruits)
# print('grape' in fruits)
# print(fruits[0])

# print(fruits['banana'])
# fruits.add('grape')
# print(fruits)
# fruits.add('mango')
# print(fruits)
# fruits.add('apple')
# print(fruits)
# fruits.add(['watermelon', 'peach'])

# fruits = {'apple', 'banana', 'cherry', 'grape'}
# fruits.remove('apple')
# print(fruits)

# # fruits.remove('pineapple')
# fruits.discard('cherry')
# print(fruits)

# immutable_fruits = frozenset(['apple', 'banana', 'cherry', range(4)])
# print('apple' in immutable_fruits)
# print('grape' in immutable_fruits)

# print(immutable_fruits[0])
# print(immutable_fruits['cherry'])
# immutable_fruits.add('grape')
# print(immutable_fruits)
# a = {range(5): 'hello', 2: 'hi'}
# print(a)
# b = tuple((1, 1, 2, 2, [1, 2]))
# print(b)
# c = frozenset({1, 1, 2, 2, 3, 3})
# print(c)

# person = {'name': 'John', 'age': 25}
# print('name' in person)
# print('height' not in person)

# fruits_set = {'apple', 'banana'}
# print('apple' in fruits_set)

# fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
# print('apple' in fruits_frozenset)

# a = frozenset('hello')
# print(a)

# person = {'name': 'John', 'age': 25}
# print(len(person))

# fruits_set = {'apple', 'banana'}
# print(len(fruits_set))

# fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
# print(len(fruits_frozenset))

# person = {'name': 'John', 'age': 25}
# print(person)
# person.clear()
# print(person)

# fruits_set = {'apple', 'banana'}
# print(fruits_set)
# fruits_set.clear()
# print(fruits_set)

# person = {'name': 'John', 'age': 25}
# for key in person:
    # print(key)

# fruits_set = {'apple', 'banana'}
# for fruit in fruits_set:
    # print(fruit)

# fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
# for fruit in fruits_frozenset:
    # print(fruit)

# list_of_pairs = [('a', 1), ('b', 2), ('c', 3)]
# print(dict(list_of_pairs))

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# zipped_pairs = zip(keys, values)
# print(dict(zipped_pairs))

# my_list = [1, 2, 2, 3, 4, 4, 4]
# print(set(my_list))

# string = 'hello'
# print(set(string))

# my_range = range(5)
# print(set(my_range)

# my_list = [1, 2, 2, 3, 4, 4, 4]
# print(frozenset(my_list))

# string = 'hello'
# print(frozenset(string))

# my_range = range(5)
# print(frozenset(my_range))

# fruit_set = {'apple', 'banana', 'cherry'}
# fruit_frozenset = frozenset(fruit_set)
# print(fruit_frozenset)

# fruit_frozenset = frozenset(['apple', 'banana', 'cherry'])
# fruit_set = set(fruit_frozenset)
# print(fruit_set)

# a = frozenset({1, 2, 3})
# print(a)