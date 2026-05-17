lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dictionary = {inner_lst[0]: inner_lst[1] for inner_lst in lst}
print(dictionary)

print(dict(lst))