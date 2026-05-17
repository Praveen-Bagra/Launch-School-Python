# data = {'name': 'Srdjan', 'age': 38, 'city': 'Belgrade'}
# print(data['name'])
# print(data['state'])
# del data['age']
# print(data)
# del data['state']
# data = {'name': 'Srdjan', 'city': 'Belgrade'}
# print('name' in data)
# print('age' in data)
# print('age' not in data)

# data = {'name': 'Srdjan', 'city': 'Belgrade'}
# data_copy = data.copy()
# print(data_copy)

# data = {
    # 'name': 'Srdjan',
    # 'city': 'Belgrade',
    # 'favorite_colors': ['blue', 'purple'],
# }

# data_copy = data.copy()
# data_copy['favorite_colors'].append('yellow')
# print(data)

# print(data.get('name', 'Default Name'))
# print(data.get('country', 'Serbia'))

# print(data.setdefault('country', 'Serbia'))
# print(data)
# print(data.setdefault('country', 'Romania'))
# print(data)

# word = 'hello'
# letter_counts = {}
# for letter in word:
    # letter_counts.setdefault(letter, 0)
    # letter_counts[letter] += 1

# print(letter_counts)

# data = {'name': 'Srdjan', 'city': 'Belgrade'}
# city = data.pop('city')
# print(city)
# country = data.pop('country', 'Unknown')
# print(country)

# data = {'name': 'Srdjan', 'city': 'Belgrade'}
# last_item = data.popitem()
# print(last_item)
# print(data)

# data = {}
# last_item = data.popitem()
# print(last_item)

# data = {
    # 'name': 'Srdjan',
    # 'city': 'Belgrade',
    # 'country': 'Unknown',
# }

# new_data = {
    # 'job': 'Software Engineer',
    # 'hobby': 'Bachata Dancing',
    # 'country': 'Serbia',
# }

# data.update(new_data)
# print(data)

# merged_data = data | new_data
# print(merged_data)
# print(data)

# data |= new_data
# print(data)

# list_data = [['name', 'Srdjan'], ['city', 'Belgrade']]
# dict_from_list = dict(list_data)
# print(dict_from_list)

# tuple_data = (('name', 'Srdjan'), ('city', 'Belgrade'))
# dict_from_tuple = dict(tuple_data)
# print(dict_from_tuple)

# fruits = {'apple', 'banana'}
# print('apple' in fruits)
# print('grape' in fruits)
# print('grape' not in fruits)

# fruits1 = {'apple', 'banana'}
# fruits2 = {'cherry', 'date'}
# fruits3 = {'apple'}
# fruits4 = {'banana', 'cherry'}

# print(fruits3.issubset(fruits1))

# print(fruits3 <= fruits1)

# print(fruits3 < fruits1)

# print(fruits3 < fruits3)

# print(fruits1.issuperset(fruits3))

# print(fruits1.issuperset(fruits4))

# print(fruits1 >= fruits4)

# print(fruits1 > fruits4)

# fruits1 = {'apple', 'banana', 'cherry'}
# fruits2 = {'banana', 'dog', 'cat'}
# print(fruits1.union(fruits2)) 
# print(fruits1)
# print(fruits2)

# print(fruits1 | fruits2)
# print(fruits1)
# print(fruits2)


# fruits1 = {'apple', 'banana', 'cherry'}
# fruits2 = {'banana', 'dog', 'cat'}

# print(fruits1.intersection(fruits2))

# print(fruits1 & fruits2)
# print(fruits1)
# print(fruits2)

# fruits1 = {'apple', 'banana', 'cherry'}
# fruits2 = {'banana', 'dog', 'cat'}

# print(fruits2.difference(fruits1))
# print(fruits1)
# print(fruits2)

# print(fruits1 - fruits2)
# print(fruits1)
# print(fruits2)

# fruits1 = {'apple', 'banana'}
# fruits2 = {'cherry', 'date'}
# fruits3 = {'apple', 'banana', 'cherry'}

# print(fruits1.isdisjoint(fruits2))

# print(fruits1.isdisjoint(fruits3))

# fruits = {'apple', 'banana'}

# fruits_copy = fruits.copy()
# print(fruits_copy)

# kfruits = {'apple', 'banana'}
# kfruits.add('cherry')
# kprint(fruits)

# kfruits.add('banana')
# kprint(fruits)

# fruits = {'apple', 'banana', 'cherry', 'orange'}
# fruits.remove('cherry')
# print(fruits)

# fruits.remove('cherry')
# fruits.discard('cherry')

# fruits.discard('orange')
# print(fruits)

# fruits.discard('orange')
# print(fruits)

# fruits.clear()
# print(fruits)

# fruits = {'apple', 'banana', 'cherry'}
# print(fruits.pop())
# print(fruits)

# print(fruits.pop())
# print(fruits)

# print(fruits.pop())
# print(fruits)

# print(fruits.pop())
# print(fruits)

# print(set('apple'))

# print(set(['apple', 'banana', 'cherry']))

# print(set({'name': 'Srdjan', 'city': 'Belgrade', 'age': 38}))

# print(frozenset('apple'))

# print(frozenset(['apple', 'banana']))
