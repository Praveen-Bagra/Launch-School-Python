lst = ['hi', 1, 'hello', 23, 'four', None, 'seven', None, 6]

def is_not_none(obj):
    return obj is not None

print(list(filter(is_not_none, lst)))
removed_none_lst = list(filter(lambda obj: obj is not None, lst))
print(removed_none_lst)


