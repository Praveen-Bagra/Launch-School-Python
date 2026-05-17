# lst = [[1, 3], [2]]
# print(lst[0])
# print(lst[0][1])

# lst[1] = 'hi there'
# print(lst)

# lst[0][1] = 5
# print(lst)

# lst = [[1], [2]]
# lst[0].append(7)
# print(lst)
# lst[0].append([9])
# print(lst)

# print(lst[0][1][0])

# lst = [{'a': 'ant'}, {'b': 'bear'}]
# lst[0]['c'] = 'cat'
# print(lst)

# lst = [3, {"b": "bear"}, (1, [2, 3, 4], 5), {6, 7}]

# print(lst[0]) # 3
# print(lst[1]) # {'b': 'bear'}
# print(lst[1]['b']) # 'bear'
# print(lst[2][1]) # [2, 3, 4]
# print(lst[2][1:]) # ([2, 3, 4], 5)
# print(lst[2][1][2]) # 4
# print(lst[3]) # {6, 7}

# tpl = (1, [2, 3], (4, 5), {'color': 'blue', 'foo': 'bar'}, {6, 7})
# print(tpl)

# dict1 = {
    # 'numbers': [41, 42],
    # 'coordinates': (43, 44),
    # 'details': {'age': 45, 'weight': 46},
    # 'items': {47, 48},
    # 'records': frozenset([49, 50]),
# }

# print(dict1)

# valid_set = {1, 2, (3, 4), frozenset([5, 6])}
# print(valid_set)

# invalid_set = {1, 2, [3, 4]}
# a = [1, 3]
# b = [2]
# lst = [a, b]
# print(lst) # [[1, 3], [2]]

# a[1] = 5
# print(lst) # [[1, 5], [2]]
# lst[0][1] = 8
# print(a) # [1, 8]

# lst = ['a', ['b', 'c']]
# new_list = lst.copy()

# new_list[0] = 'x1'
# new_list[1][0] = 'x2'

# print(lst) # ['a', ['x2', 'c']]
# print(new_list) # ['x1', ['x2', 'c']]

# lst = ['a', 'b', 'c']
# copy_of_lst = list(lst)
# print(copy_of_lst)
# print(copy_of_lst is lst)

# lst = ['a', 'b', 'c']
# copy_of_lst = lst[:]
# print(copy_of_lst) # ['a', 'b', 'c']
# print(copy_of_lst is lst) # False

# lst = ['a', 'b', 'c']
# copy_of_lst = lst.copy()
# print(copy_of_lst) # ['a', 'b', 'c']
# print(copy_of_lst is lst) # False

# import copy

# lst = ['a', 'b', 'c']
# copy_of_lst = copy.copy(lst)
# print(copy_of_lst) # ['a', 'b', 'c']
# print(copy_of_lst is lst) # False

# lst = [['a'], ['b'], ['c']]
# copy_of_lst = lst.copy()

# copy_of_lst[1].append('d')
# print(lst) # Prints [['a'], ['b', 'd'], ['c']]
# print(copy_of_lst) # Prints [['a'], ['b', 'd'], ['c']]
# print(copy_of_lst is lst) # Prints False

# lst = [{'a': 'foo'}, {'b': 'bar'}, {'c': 'baz'}]
# copy_of_lst = lst.copy()

# copy_of_lst[1]['d'] = 7
# print(lst) # Prints [{'a': 'foo'}, {'b': 'bar', 'd': 7}, {'c': 'baz'}]
# print(copy_of_lst) # Prints [{'a': 'foo'}, {'b': 'bar', 'd': 7}, {'c': 'baz'}]
# print(copy_of_lst is lst) # Prints False

# dict1 = {'a': 'foo', 'b': 'bar'}
# copy_of_dict1 = dict1.copy()

# print(copy_of_dict1) # Prints {'a': 'foo', 'b': 'bar'}
# print(copy_of_dict1 is dict1) # Prints False

# copy_of_dict1['c'] = 'baz'
# print(copy_of_dict1) # Prints {'a': 'foo', 'b': 'bar', 'c': 'baz'}
# print(dict1) # {'a': 'foo', 'b': 'bar'} 

# dict1 = {'a': {'b': 1}, 'c': [2]}
# copy_of_dict1 = dict1.copy()

# dict1['a']['d'] = 42
# dict1['c'].append(3.14)
# print(copy_of_dict1) # {'a': {'b': 1, 'd': 42}, 'c': [2, 3.14]}
# print(dict1) # {'a': {'b': 1, 'd': 42}, 'c': [2, 3.14]}

# import copy

# lst = ['a', ['b', 'c']]
# new_lst = copy.deepcopy(lst)

# new_lst[0] = 'x1'
# new_lst[1][0] = 'x2'

# print(lst) # ['a', ['b', 'c']]
# print(new_lst) # ['x1', ['x2', 'c']]

import copy

lst= [{'b': 'foo'}, ['bar']]
deep_copied_lst = copy.deepcopy(lst)

deep_copied_lst[1].append('baz')
print(deep_copied_lst) # [{'b': 'foo'}, ['bar', 'baz']]
print(lst) # [{'b': 'foo'}, ['bar']]

