lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_lst = []
for inner_lst in lst:
    sorted_lst.append(sorted(inner_lst))

print(sorted_lst)
print(lst)

sorted_lst = [sorted(inner_lst) for inner_lst in lst]
print(sorted_lst)
print(lst)