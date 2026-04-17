dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# It would print [1, 42, 3] since dict2 = dict(dict1) on line 6 created a 
# shallow copy. dict2['a'] and dict1['a'] refers to the same object. So when 
# we mutated this object, the exchange will reflect in other dictonary too. 