dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
# Prints ('b', 'bear'). It mutates the caller (i.e. original dictionary)
# and returns the last key, value pair as tuple
print(dictionary)